from numpy import *
import matplotlib.pyplot as plt

from cdflib import *
from pprint import *
def local_cdf_import():
    fname = "./data/ac_h2_epm_20190101_v06.cdf"
    cdf = CDF(fname)
    ## Low-Energy Magnetic Spectrometer (30)
    ## P1-P8 [1/(cm^2 s sr MeV)]
    t   = [cdf.varget("Epoch")][0]
    x   = [cdf.varget("P1"),
           cdf.varget("P2"),
           cdf.varget("P3"),
           cdf.varget("P4"),
           cdf.varget("P5"),
           cdf.varget("P6"),
           cdf.varget("P7"),
           cdf.varget("P8")]

    for i in range(len(x)):
        plt.scatter(t, x[i])

    plt.show()
    pprint(t)

def mp3_import():
    from lxml import html, etree
    import requests
    # Get the original webpage html content
    webpageLink = 'https://sdo.gsfc.nasa.gov/assets/img/latest/20170706_144133_1024_211193171.jpg'
    page = requests.get(webpageLink)
    # convert the data received into searchable HTML
    extractedHtml = html.fromstring(page.content)
    # use an XPath query to find the image link (the 'src' attribute of the 'img' tag).
    imageSrc = extractedHtml.xpath("//img/@src") # in our example, result = ‘/images/GrokkingAlgorithms.jpg’
    print(imageSrc)
    # strip off the actual *page* being called as we only want to base url
    imageDomain = webpageLink.rsplit('/', 1) # in our example, result = http://www.howtowebscrape.com/examples/
    # test if this is an absolute link or relative
    if imageSrc[0].startswith("http"):
        # start with http, therefore take this as the full link
        imageLink = imageSrc[0]
    else:
        # does not start with http, therefore construct the full url from the base url plus the absolute image link
        imageLink = str(imageDomain[0]) + str(imageSrc[0])
    # extract file name from link
    filename = imageLink.split("/")[-1]
    # download image using GET
    rawImage = requests.get(imageLink, stream=True)
    # save the image received into the file
    with open(filename, 'wb') as fd:
        for chunk in rawImage.iter_content(chunk_size=1024):
            fd.write(chunk)

def web_cdf_import():
    import requests
    date    = '2019' + '02' + '20' + "12"
    # snsr    = 'fld_l2_dfb_ac_bpf_dv34'
    snsr    = 'fld_l2_mag_sc'
    fname   = 'psp_{}_{}_v01.cdf'.format(snsr,date)
    url     = 'https://cdaweb.gsfc.nasa.gov/pub/data/psp/fields/l2/mag_sc/2019/' + fname
    r   = requests.get(url, allow_redirects=True)
    open(fname, 'wb').write(r.content)
    cdf = CDF(fname)
    pprint(cdf.cdf_info())
    pprint(cdf.varget('psp_fld_l2_mag_SC_MET'))
    pprint(cdf.attget('UNITS', 1))
    label   = cdf.varget('label_SC')
    t       = (cdf.varget('epoch_mag_SC')/3.15e16)
    mag_sc  = cdf.varget('psp_fld_l2_mag_SC')

    fig, ax = plt.subplots()
    for i in range(len(mag_sc[0])):
        plt.scatter(t,[dt[i] for dt in mag_sc], s=0.5)
    plt.legend(label[0])
    ax.ticklabel_format(useOffset=False)
    plt.xlim(min(t), max(t))
    plt.ylabel("Magnetic Field (nT)")
    plt.xlabel("Epoch (yr)")
    plt.show()
web_cdf_import()
