from __future__ import print_function
import glob
import os
from optparse import OptionParser

def mkndir(path,verb=False):
    success = False
    if not os.path.exists(path):
        if verb:
            print( "Making ",path)
        try:
            os.mkdir(path)
            success = True
        except Exception as e :
            print( "cannot make",path,e)
    else:
        success = True
        # we were successful at nothing!
    return success

def lnkfile(infile,outpath,verb=False):

    infilename = os.path.basename(infile)
    outfile = os.path.join(outpath,infilename)

    try:
        if verb:
            print("linking",infile,outfile)
        if os.path.exists(outfile):
            if verb:
                print( outfile, "exists")
                os.remove(outfile)
                os.link(infile,outfile)
        else:
            os.link(infile,outfile)
    except Exception as e:
        print( e)
        exit()
    return

parser = OptionParser()
parser.add_option("-d", "--dir", dest="installdir", default = "../wsgi-scripts/",
                  help="destination directory, can be relative or absolute")
parser.add_option("-v", "--verbose",
                  action="store_true", dest="verbose", default=False,
                  help="print status messages to stdout")

(options,args) = parser.parse_args()

cwdir = os.path.dirname(os.path.abspath(__file__))


abspath = os.path.abspath(options.installdir)
verb = options.verbose
if not mkndir(abspath,verb):
    exit()

filelist = ["web_s2n.wsgi","idl_wrapper","env-for-xidl"]
filelist += glob.glob("*.py")

try:
    for f in filelist:
        # os.link(f,os.path.join(abspath,f))
        lnkfile(f,abspath,verb)
except Exception as e :
    print( "cannot link",f,e)
    exit()

viewdir = os.path.join(abspath,"views")

if not mkndir(viewdir,verb):
    exit()

dfiles = glob.glob(os.path.join(cwdir,"views") + "/*.tpl")
for df in dfiles:
    lnkfile(df,viewdir,verb)

viewdirlist = ["css","javascript"]
for vd in viewdirlist:
    abscd = os.path.join(cwdir,"views",vd)
    absvd = os.path.join(abspath,"views",vd)
    if not mkndir(absvd,verb):
        exit()

    gstr = abscd + "/*.*"
    dfiles = glob.glob(gstr)

    for df in dfiles:
        lnkfile(df,absvd,verb)
