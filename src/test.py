import matplotlib.pyplot as plt

from sunpy.net import Fido, attrs as a
import sunpy.map
from sunpy.io.file_tools import read_file

import matplotlib.pyplot as plt
from reproject import reproject_interp

import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.wcs import WCS

import warnings
import os, contextlib
from rich.progress import track
import time
import datetime
from calendar import monthrange

from rich import print
from rich.console import Console
from rich.panel import Panel

import requests # to get image from the web
import shutil # to save it locally

from pyexiv2 import ImageMetadata
import json, datetime
import geocoder
import pprint

from parfive import Downloader
console = Console()
from astropy.utils.exceptions import AstropyWarning
warnings.filterwarnings("ignore", category=AstropyWarning)

from rich.progress import (
    BarColumn,
    DownloadColumn,
    TextColumn,
    TransferSpeedColumn,
    TimeRemainingColumn,
    Progress,
    TaskID,
)


progress = Progress(
    TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
    BarColumn(bar_width=None),
    "[progress.percentage]{task.percentage:>3.1f}%",
    TimeRemainingColumn(),
)
progress1 = Progress()

def write(fname, instr,date,time,xaxis,yaxis,xunits,yunits,filter):
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

import sunpy.data.sample
def test1():
    timerange = a.Time('2019/05/02 00:00', '2019/05/02 00:01')
    instrument = a.Instrument('LASCO')
    detector = a.Detector('C1')
    result = Fido.search(timerange, instrument)

    print(result)

    downloaded_files = Fido.fetch(result)
    print(downloaded_files)

    data, header = read_file(downloaded_files[0])[0]

    # Add the missing meta information to the header
    header['CUNIT1'] = 'arcsec'
    header['CUNIT2'] = 'arcsec'

    lascomap = sunpy.map.Map(data, header)
    fig = plt.figure()
    lascomap.plot()
    plt.show()

def test2(dfile, fname):
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

def test3(fname):
    metadata = ImageMetadata(fname)
    metadata.read()
    userdata=json.loads(metadata['Exif.Photo.UserComment'].value)
    pprint.pprint(userdata)

import sys

def download(instr,detec,syear,eyear):
    """Download multuple files to the given directory."""
    progress.log("[blue]Beginning script")
    with progress:
        am = m = 0
        year    = syear
        start_date  = datetime.date(syear,1,1)
        end_date    = datetime.date(eyear,2,1)

        task_id = progress.add_task("download", filename="{} {}: {}".format(instr,detec, year))

        while am <= (11 * (end_date.year - start_date.year)):
            if am < 11:
                m = am
            elif am == 11:
                year = syear + 1
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
                    test2(dfiles, str(dfiles[0]))
                    os.remove(str(dfiles[0]))
                    progress.update(task_id_1, advance=100./n)
                except requests.exceptions.ConnectionError:
                    dt = 5
                    task_id_2 = progress1.add_task("[bold yellow]Connection Error: Retrying...")
                    while not progress1.finished:
                        time.sleep(dt)
                        dfiles  = Fido.fetch(result[0,i], progress=False, overwrite=True, path=pname)
                        test2(dfiles, str(dfiles[0]))
                        os.remove(str(dfiles[0]))
                        progress1.update(task_id_2, advance=100./(60. * dt))
                    progress.update(task_id_1, advance=100./n)
            progress.log("[green]Fetch complete")

            am += 1

            start_date += datetime.timedelta(days=days)
            end_date += datetime.timedelta(days=days)
            progress.update(task_id, advance=100./(11))

    progress.log("[blue]Script complete")
download('LASCO', 'C3', 2000, 2000)
# test3("/media/pharaohcola13/SALSA/LASCO/C3/2000/1/22058870.png")
