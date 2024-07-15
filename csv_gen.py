import os
import os.path
try:
    from cStringIO import StringIO
except:
    from io import StringIO

def csv_output(input):
    # this needs to reformat output into a csv file
    # wave,obj,sky,noise,s2n
    # input consists of a dictionary of arrays
    # each array (obj, sky, etc.) is actually a pair of values

    tempd = {}

    for key in ['wave','s2n','sky','obj','noise']:
        tempd[key] = []
        for i in range(0,len(input[key])):
            if key == 'wave':
                tempd[key].append(input[key][i])
            else:
                tempd[key].append(input[key][i][1])


    csvfile = StringIO()
    csvfile.write("wave,obj,sky,noise,s2n\n")
    for i in range(0,len(tempd['wave'])):
        tstr = ""
        for key in ['wave','obj','sky','noise','s2n']:
            tstr += str(tempd[key][i]) + ","
        tstr = tstr.rstrip(',')
        tstr += "\n"
        csvfile.write(tstr)


        
    
    return csvfile.getvalue()
