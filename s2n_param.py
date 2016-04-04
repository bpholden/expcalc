import subprocess as sub
import re
import os, os.path


def bad_obj(objcts):
    bad = False
    nbad = 0
    print objcts
    for pair in objcts:
        wv,oc = pair
        if oc < 0:
            nbad += 1
        if nbad > 5:
            bad = True
    print bad
    return bad

def parse_return(output,idlout):

    lines = idlout.splitlines()

    inline = 0
    curkey = ''
    for line in lines:
        match = re.search('\A(\w+)\:',line)
        if match:
            if match.group(1) in output.keys():
                curkey = match.group(1)
                inline = 1
                output[curkey]= line.split()[1:]
            
        elif inline == 1:
            output[curkey].extend(line.split())


    temp = []
    for i,wv in enumerate(output['wave']):
        t = []
        temp.append([float(wv),float(output['obj'][i]),float(output['sky'][i]),float(output['noise'][i]),float(output['s2n'][i])])
    output['cts'] = temp

    for key in ['s2n','sky','obj','noise']:
        temp = []
        jtemp = []
        jkey = "j%s" % (key)
        for i,wv in enumerate(output['wave']):
            temp.append([float(wv),float(output[key][i])])
            jtemp.append(float(output[key][i]))
        output[key] = temp
        output[jkey] = jtemp
        
    nwave = []
    for wv in output['wave']:
        nwave.append(float(wv))
    output['wave']=nwave

    if bad_obj(output['obj']):
        output["errormsg"] = "The selected filter and template do not overlap. Please select another filter, another template, or redshift the template. "
        

    return(output)

def parse_request(value,regexp,name):

    msg = ""
    match = re.search(regexp,value)
    if match:
        cleanvalue = match.group(0)
    else:
        cleanvalue = -1
        msg = "Inappropriate value for the input parameter %s" % name


    return cleanvalue,msg

def paramandvals(param,paramval):

    str=""
    match = re.search("\A\d+\.?\d*\Z",paramval)
    if match:
        str= "%s=%s," % (param,paramval)
    else:
        str= "%s='%s'," % (param,paramval)
    return(str)

def strip_badchar(com):

    # really need to get rid of $, ; and ``

    #    ncom,nvals = re.subn("(\$|\;|\`)","",com)
    #    print com,
    ncom,nvals = re.subn("[^a-zA-Z0-9_/,'=.]","",com)
    #    print ncom,nvals
    return ncom,nvals

def build_exec_str(com,paramregexp,prettyparam,params):

    output = dict(wave = [],
                  s2n = [],
                  obj = [],
                  objperwavesec = [],
                  noise = [],
                  sky = [],
                  com = "",
                  dich = "",
                  msg = '',
                  errormsg = '',
                  i2counts = None,
                  exp = None,

        )


    for param in prettyparam.keys():
        if param in params.keys() and params[param]:
            paramval,output['msg'] = parse_request(params[param],paramregexp[param],prettyparam[param])

            if param == 'dichroic':
                output['dich'] = paramval
            if output['msg']:
                return "",output
            else:
                com += paramandvals(param,paramval)

            
    com = com.rstrip(',')
    return com,output


def gen_s2n(com,output,verbose,wsgi_dir):


    com,nvals = strip_badchar(com)
    if nvals:
        output['msg'] = "Input values had some unexpected characters"
    if len(com) == 0:
        output['msg'] = "Command string has no characters"
        return output
    output['com'] = com
    runargs = []
    runargs.append(os.path.join(wsgi_dir,'idl_wrapper') )
    #    runargs.append("-e")
    #    runargs.append( '"' + com + '"' )
    if verbose:
        print "path:",os.path.join(wsgi_dir,'idl_wrapper')
        print "com:",com
        print "runargs:", runargs

    try:
        p = sub.Popen(runargs,stdin=sub.PIPE,stdout=sub.PIPE,stderr=sub.PIPE)
        # we can rethink this now that we use idl_wrapper
        idlout,idlerr=p.communicate(com)
        if verbose:
            print idlout
            print idlerr
            # print output
            #    output['msg'] = idlerr
        output = parse_return(output,idlout)
    except:
        output['msg'] = "Server side error, email holden@ucolick.org."

    return output
