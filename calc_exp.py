from __future__ import print_function
import sys
import json
import urllib
import urllib2
from cookielib import CookieJar
from optparse import OptionParser
import templates_filters

class LConn():
    def __init__(self,host="",port=0):
        self.port = port
        self.host = host
        self.cj = CookieJar()
        self.opener = ''

    def __repr__(self):
        return "LConn %s:%d" % (self.host,self.port)

    def post_url(self,url,indict,debug=False):


        if self.port:
            fullurl = "http://%s:%d%s" % (self.host,self.port,url)
        else:
            fullurl = "http://%s%s" % (self.host,url)
        params = urllib.urlencode(indict)

        if debug:
            print(fullurl + params)

        if not self.opener:
            self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))

        try:
            res = self.opener.open(fullurl,params)
            retval = res.read()
        except urllib2.URLError as e:
            return '',str(e)
        except urllib2.HTTPError as e:
            return '',str(e)

        return retval,''


    def binning_opts(self,indict):

        if indict['inst'] == "apf":
            #spatial by spectral
            (spatial,spectral) = indict["binning"].split("x")
            indict["spatialbinning"] = spatial
            indict["spectralbinning"] = spectral
            del indict['binning']

    def calc_s2n(self,options):

        indict = { 'mag': options.mag.strip("'"),
                   'template' : options.temp.strip("'"),
                   'seeing' : options.seeing.strip("'"),
                   'slitwidth' : options.slitwidth.strip("'"),
                   'binning' : options.binning.strip("'"),
                   'ffilter' : options.ffilter.strip("'"),
                   'mtype' : 2,
                   'inst' :  options.inst.strip("'"),
                   'redshift' : options.redshift.strip("'"),
                   'airmass' : options.airmass.strip("'"),
                   'exptime' : options.exptime.strip("'"),
                   }
        mag_sys =  options.sys.strip("'")
        if mag_sys == 'Vega':
            indict['mtype']=1

        self.binning_opts(indict)

        if options.debug:
            url = "/gen_inst_s2n"
        else:
            url = "/web_s2n/gen_inst_s2n"
        ret_val,errmsg = self.post_url(url,indict,debug=options.debug)
        return ret_val,errmsg


def lookup_template(options):
    (templates,tabbr) = templates_filters.get_templates()
    template = ""
    for i, tname in enumerate(tabbr):
        if options.temp in tname:
            template = templates[i]

    if options.debug:
        print(options.temp, template)
    options.temp = template

def ffilter(options):
    options.ffilter = "sdss_%s.dat" % (options.ffilter)

def unwrap_output(ret_val):

    output = json.loads(ret_val)
    if 'msg' in output and output['msg']:
        outstr = output['msg']
        return outstr
    out_vals = ["# wave  s2n obj sky rn "]
    for i in range(len(output['noise'])):
        outstr = "%.2f %.2f " % (output['s2n'][i][0],output['s2n'][i][1])
        outstr += "%.2f " % (output['obj'][i][1])
        outstr += "%.2f " % (output['sky'][i][1])
        outstr += "%.2f " % (output['noise'][i][1])
        out_vals.append(outstr)
    return out_vals


parser = OptionParser()
# observation options
parser.add_option("-m", "--mag", dest="mag",default="13.0",
                  help="magnitude value")
parser.add_option("-s","--system", dest="sys",default="AB",
                  help="type of magnitude (AB or Vega)")
parser.add_option("-t","--temp", dest="temp",default="K0V",
                  help="Spectral template (A5V or E or Sb)")
parser.add_option("-z","--redshift", dest="redshift",default="0.0",
                  help="redshift of object")
parser.add_option("-a","--airmass", dest="airmass",default="1.1",
                  help="Airmass")
parser.add_option("-e","--exptime", dest="exptime",default="1200",
                  help="Exposure time in seconds ")
parser.add_option("-f","--fwhm", dest="seeing",default="1.2",
                  help="fullwidth at half maximum of the seeing")

# instrument options
parser.add_option("-i","--inst", dest="inst",default="apf",
                  help="Instruments (kast hires esi deimos apf)")
parser.add_option("-w","--slitwidth", dest="slitwidth",default="1.0",
                  help="width of slit")
parser.add_option("-c","--dichroic", dest="dichroic",default="d55",
                  help="Kast dichroic (d55 or d46)")
parser.add_option("-l","--filter", dest="ffilter",default="r",
                  help="filter to normalize the template (u g r i z)")
parser.add_option("-b","--binning", dest="binning",default="1x1",
                  help="Binning of data on detector (spatial x spectra")
parser.add_option("-d","--debugging", dest="debug",default=False,
                  action="store_true",
                  help="debugging flag, runs on donut, prints stuff ")

(options, args) = parser.parse_args()
lookup_template(options)
ffilter(options)

if options.debug:
    lconn = LConn(host="donut.ucolick.org",port=9020)
else:
    lconn = LConn(host="etc.ucolick.org",port=80)
retval,msg = lconn.calc_s2n(options)
if msg:
    print(msg)
    sys.exit()
out= unwrap_output(retval)
for line in out:
    print(line)
