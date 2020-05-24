import pprint
import requests
import warnings
import sunpy.map
import datetime, time
import os, contextlib, sys
from calendar import monthrange
import matplotlib.pyplot as plt
from reproject import reproject_interp

from astropy.wcs import WCS
from sunpy.net import Fido, attrs as a
from sunpy.io.file_tools import read_file
from astropy.utils.exceptions import AstropyWarning

import json
from pyexiv2 import ImageMetadata

from rich import print
from rich.panel import Panel
from rich.progress import track
from rich.console import Console

from rich.progress import (
BarColumn,
DownloadColumn,
TextColumn,
TransferSpeedColumn,
TimeRemainingColumn,
Progress,
TaskID,
)
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description='Data Extraction for SALSA', formatter_class=RawTextHelpFormatter)

parser.add_argument("-I","--instrument", action="store", type=str, dest="I",
                    help='Instrument')
parser.add_argument("-D", "--detector",  action="store", type=str, dest="D",
                    help='Detector')
parser.add_argument("-sd", "--start_date", action="store", type=str, dest="sd",
                    help='Start Date\n\t[Default: 2000/01/01]', default="2000/01/01")
parser.add_argument("-ed", "--end_date", action="store", type=str, dest="ed",
                    help='End Date\n\t[Default: 2001/01/01]', default="2001/01/01")

args = parser.parse_args()

console = Console()
warnings.filterwarnings("ignore", category=AstropyWarning)

progress = Progress(
    TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
    BarColumn(bar_width=None),
    "[progress.percentage]{task.percentage:>3.1f}%",
    TimeRemainingColumn(),
)
progress1 = Progress()

class extraction:
    def write(self, fname, instr,date,time,xaxis,yaxis,xunits,yunits,filter):
        metadata    = ImageMetadata(fname)
        metadata.read()

        userdata = {'File name' : fname,
                    'Instrument': instr,
                    'Date'      : date,
                    'Time'      : time,
                    'X-Axis'    : xaxis,
                    'X-units'   : xunits,
                    'Y-units'   : yunits,
                    'Y-Axis'    : yaxis,
                    'Filter'    : filter,
                    }
        metadata['Exif.Photo.UserComment'] = json.dumps(userdata)
        metadata.write()

    def meta(self, dfile, fname):
        data, header = read_file(dfile[0])[0]
        # Add the missing meta information to the header
        header['CUNIT1'] = 'arcsec'
        header['CUNIT2'] = 'arcsec'

        ax = sunpy.map.Map(data, header)
        fig = plt.figure()
        ax.plot()

        instr       = str(header['TELESCOP'] + "-"  + header['INSTRUME'] + "-" + header['DETECTOR'])
        date        = str(header['DATE-OBS'])
        time        = str(header['TIME-OBS'])
        filter      = str(header['FILTER'])
        ylabel      = str(header['CTYPE2'])
        xlabel      = str(header['CTYPE1'])

        img_name    = fname.split(".")[0] + ".png"
        plt.savefig(img_name)

        write(img_name, instr, date, time,
                xlabel,ylabel,"arcsec","arcsec",filter)

        plt.close()

    def test3(self, fname):
        metadata = ImageMetadata(fname)
        metadata.read()
        userdata=json.loads(metadata['Exif.Photo.UserComment'].value)
        pprint.pprint(userdata)

    def download(self,instr,detec,sdate,edate):
        """Download multuple files to the given directory."""
        progress.log("[blue]Beginning script")
        with progress:
            am = m = 0
            end_date    = datetime.datetime.strptime(edate, "%Y/%m/%d")
            start_date  = datetime.datetime.strptime(sdate, "%Y/%m/%d")
            year        = start_date.year

            task_id = progress.add_task("download", filename="{} {}: {}".format(instr,detec, year))

            while am <= (11 * (end_date.year - start_date.year)):
                if am < 11:
                    m = am
                elif am == 11:
                    year =+ 1
                    m = am - 11
                else:
                    m = am - 11

                task_id_1 = progress.add_task("download", filename="Y: {}; M: {}".format(year, 1+m))
                days = monthrange(year, 1 + m)[1]
                timerange = a.Time(start_date, end_date)

                instrument  = a.Instrument(instr)
                progress.log("[yellow]Beginning search")

                result      = Fido.search(timerange, instrument)
                n = len(result.get_response(0))

                progress.log("[green]Search complete: Found {} files".format(n))
                progress.log("[yellow]Beginning fetch")
                for i in range(0, n):
                    pname   = "/media/pharaohcola13/SALSA/{}/{}/{}/{}/".format(instr,detec,year,1 + m)
                    try:
                        dfiles  = Fido.fetch(result[0,i], overwrite=True, path=pname, progress=False)
                        meta(dfiles, str(dfiles[0]))
                        os.remove(str(dfiles[0]))
                        progress.update(task_id_1, advance=100./n)
                    except requests.exceptions.ConnectionError:
                        dt = 5
                        task_id_2 = progress1.add_task("[bold yellow]Connection Error: Retrying...")
                        while not progress1.finished:
                            time.sleep(dt)
                            dfiles  = Fido.fetch(result[0,i], progress=False, overwrite=True, path=pname)
                            meta(dfiles, str(dfiles[0]))
                            os.remove(str(dfiles[0]))
                            progress1.update(task_id_2, advance=100./(60. * dt))
                        progress.update(task_id_1, advance=100./n)
                progress.log("[green]Fetch complete")

                am += 1

                start_date += datetime.timedelta(days=days)
                end_date += datetime.timedelta(days=days)
                progress.update(task_id, advance=100./(11))

        progress.log("[blue]Script complete")
extraction().download(args.I, args.D, args.sd, args.ed)
