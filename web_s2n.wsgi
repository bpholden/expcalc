from __future__ import print_function
from bottle import route, run, debug, template, request, static_file, error, default_app, response
import subprocess as sub
import os, os.path, sys
from optparse import OptionParser

import templates_filters
from insts import Inst
from s2n_param import gen_s2n, build_exec_str
from csv_gen import csv_output

wsgi_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(wsgi_dir)
sys.path.append(wsgi_dir)


parser = OptionParser()
parser.add_option("-d", "--devel", dest="devel", default=False,
                  action="store_true",help="run using bottle's WSGI server")
parser.add_option("-l", "--local", dest="local", default=False,
                  action="store_true",help="run only on localhost instead of on hostname")
parser.add_option("-v", "--verbose",
                  action="store_true", dest="verbose", default=False,
                  help="print status messages to stdout")

(options, args) = parser.parse_args()

devel = options.devel
local = options.local
verbose = options.verbose

@route('/lris')
def lris():

    filters,fabbr = templates_filters.get_filters()
    templates,tabbr = templates_filters.get_templates()
    output = template('make_lris_form',inst="lris",
                  filters = filters,
                  fabbr = fabbr,
                  tabbr = tabbr,
                  templates = templates
        )
    return output


@route('/kast')
def kast():

    filters,fabbr = templates_filters.get_filters()
    templates,tabbr = templates_filters.get_templates()
    output = template('make_kast_form',inst="kast",
                  filters = filters,
                  fabbr = fabbr,
                  tabbr = tabbr,
                  templates = templates
        )
    return output

@route('/deimos')
def deimos():

    filters,fabbr = templates_filters.get_filters()
    templates,tabbr = templates_filters.get_templates()
    output = template('make_deimos_form',inst="deimos",
                      filters = filters,
                      fabbr = fabbr,
                      tabbr = tabbr,
                      templates = templates
        )
    return output

@route('/esi')
def esi():

    filters,fabbr = templates_filters.get_filters()
    templates,tabbr = templates_filters.get_templates()
    output = template('make_esi_form',inst="esi",
                      filters = filters,
                      fabbr = fabbr,
                      tabbr = tabbr,
                      templates = templates
                      )
    return output

@route('/apf')
def apf():

    filters,fabbr = templates_filters.get_star_filters()
    templates,tabbr = templates_filters.get_star_templates()
    output = template('make_apf_form',inst="apf",
                      filters = filters,
                      fabbr = fabbr,
                      tabbr = tabbr,
                      templates = templates
                      )
    return output

@route('/testapf')
def testapf():
    
    filters,fabbr = templates_filters.get_filters()
    templates,tabbr = templates_filters.get_templates()
    output = template('make_testapf_form',inst="apf",
                      filters = filters,
                      fabbr = fabbr,
                      tabbr = tabbr,
                      templates = templates
                      )
    return output

@route('/hires')
def hires():
    
    filters,fabbr = templates_filters.get_filters()
    templates,tabbr = templates_filters.get_templates()
    output = template('make_hires_form',inst="hires",
                      filters = filters,
                      fabbr = fabbr,
                      tabbr = tabbr,
                      templates = templates	      
                      )
    return output


@route('/gen_inst_s2n',method='ANY')
def gen_inst_s2n():
    instr = Inst()
    instr = instr.make(request.params['inst'])

    if devel:
        for k in request.params.keys():
            print( "gen_inst_s2n ",k, request.params[k])
    com,output = build_exec_str(instr.com,instr.paramregexp,instr.prettyparam,request.params)
    if devel:
        print( "gen_inst_s2n ",com)
        print( "gen_inst_s2n ",output)
    if not output['msg']:
        output = gen_s2n(com,output,verbose,wsgi_dir)

    return output


@route('/tab_s2n',method='GET')
def tab_s2n():

    instr = Inst()
    instr = instr.make(request.query.inst)
    com,output = build_exec_str(instr.com,instr.paramregexp,instr.prettyparam,request.params)
    output = gen_s2n(com,output,verbose,wsgi_dir)

    #    return static_file(tfname, root=tfdir, download=tfname)

    filename = "%s_tab.csv" % (request.query.inst)

    response.set_header('Pragma','public')
    response.set_header('Expires','0')
    response.set_header('Cache-Control','must-revalidate, post-check=0, pre-check=0')
    response.set_header('Content-type','application/csv')
    response.add_header('Content-type','application/force-download')
    response.set_header('Content-Transfer-Encoding','binary')
    response.set_header('Content-Disposition','attachment;filename=%s ' % (filename))


    csvs = csv_output(output)

    return csvs


@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'

@error(405)
def mistake405(code):
    return 'Sorry, method invalid or something (aka 405)'


@route('/javascript/:name')
def javascript(name):
    try:
        retval = static_file(name, root='views/javascript/', mimetype='text/javascript')
    except:
        retval = name
    return retval

@route('/css/:name')
def css(name):

    return static_file(name, root='views/css/', mimetype='text/css')

@route('/views/:name')
def views(name):

    return static_file(name, root='views/', mimetype='text/html')


###
# begin the begin
###



debug(True)
#run(server='cherrypy',reloader=True)
application = default_app()
if devel:
    if local:
        run(application, reloader=True,port=9020)
    else:
        hostname = os.getenv('HOSTNAME')
        run(application, reloader=True,port=9020,host=hostname)
