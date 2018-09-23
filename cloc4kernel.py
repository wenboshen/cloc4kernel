import os

from subprocess import call
from shutil import copyfile

copy_suffix= ["c", "C", "s", "S"] 

os.system("find . -name \"*.o\" > object_files")

with open("object_files") as objfile:
    for line in objfile:
        filename = line.strip()[:-1]
        for suffix in copy_suffix:
	    tocopy = filename+suffix
	    if os.path.isfile(tocopy):
		newfile = "../cloc/"+tocopy
		newpath = os.path.dirname(newfile)
		if not os.path.exists(newpath):
		    os.makedirs(newpath)
		print tocopy
		copyfile(tocopy, newfile)
                break

## handle for header files
search_dirs = ['./include/', './arch/arm64/include/']
os.system("grep \"#include\" ../cloc -ir > header_files")
with open("header_files") as headerfile:
    for line in headerfile:
        line = line.strip()
        #print line[-1]
        tokens = line.split() 
        cfile = tokens[0]
        line = tokens[-1]
        if line.endswith('>'):
            for header_dir in search_dirs:
                tocopy = header_dir + line[1:-1] 
                if os.path.isfile(tocopy):
    		    newfile = "../cloc/"+tocopy
    		    newpath = os.path.dirname(newfile)
    		    if not os.path.exists(newpath):
    		        os.makedirs(newpath)
    		    #print tocopy
    		    copyfile(tocopy, newfile)
                    break

        if line.endswith('"'):
            print line[1:-1]
            cfile = cfile.strip()
            cfile = cfile.split(':')[0]
            cfile = cfile[8:]
            pathname = os.path.dirname(cfile)
            #print cfile
            #print pathname
            tocopy = pathname + '/'+ line[1:-1] 
            if os.path.isfile(tocopy):
    		newfile = "../cloc/"+tocopy
    		newpath = os.path.dirname(newfile)
    		if not os.path.exists(newpath):
    		    os.makedirs(newpath)
    		print tocopy
    		copyfile(tocopy, newfile)
    


