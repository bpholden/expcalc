from __future__ import print_function
from optparse import OptionParser
import subprocess as sub
import asciitable


parser = OptionParser()
parser.add_option("-t", "--test", dest="testing", default=False,
                  action="store_true",help="Just testing")
parser.add_option("-v", "--verbose",
                  action="store_true", dest="verbose", default=False,
                  help="print status messages to stdout")

(options, args) = parser.parse_args()

testing = options.testing
verbose = options.verbose

etchostname = "etc.ucolick.org/web_s2n"
if testing:
    etchostname = "donut:9020"

exec_str = "%s/tab_s2n" % (etchostname)
exec_str += '?slitwidth=0.75&binning=1x1&exptime=3600.0&mag=17.0&ffilter=sdss_r.dat&mtype=2&seeing=0.75&template=s0_template.fits&inst=esi&airmass=1.1&redshift=0.0'
if verbose:
    print(exec_str)

com = 'curl "' + exec_str +'"'
if verbose:
    print(com)
retval = sub.check_output(com,shell=True)
if verbose:
    print(retval)
refdata = asciitable.read("test_results.csv")
retvals = retval.split('\n')
if len(retvals) == (len(refdata)+2):
    print("Success: system up and working")
else:
    print("Return data not correct")
