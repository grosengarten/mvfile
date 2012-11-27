##movefile.py
##moves/copies a file
##greg rosengarten - 11/16/2012

import sys,os, glob, shutil 
from age import *

def movefile(source,mask,dest, _cp=False):

    mv = shutil.copy2 if _cp else shutil.move
    ##check for undefined args
    ##if not source or mask or dest:
        ##return None
    
    ##get file to move
    gob = os.path.join(source,mask)
    list_of_files = glob.glob(gob)
    if not list_of_files:
        print "No files match the glob %s" %gob
        sys.exit(1)
    else:
        file = get_oldest_file(list_of_files)
    
    ## move the file
    mv(file,dest)
    
    ## return the resulting filename and path moved
    name = os.path.basename(file)
    resultstr = os.path.join(dest,name)
    
    return resultstr    

def main():
    
    for arg in sys.argv[1],sys.argv[3]:
	## check each directory exists
            if os.path.exists(arg):
                continue
            else:
                print "directory '%s' doesn't exist. Exiting." % arg
                break

    try:
        print movefile(sys.argv[1],sys.argv[2],sys.argv[3])
    except shutil.Error:
        print "Dest file already exists."
        sys.exit(1)
        '''
    except WindowsError:
        "File not removed.  Write permissions unavailable on '%s'" % sys.argv[3]
        sys.exit(1)
        '''
## main execution here
if __name__ == "__main__":
    main()
      
