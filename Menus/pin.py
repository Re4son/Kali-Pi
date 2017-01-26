#!/usr/bin/env python
import sys, os, hashlib, getpass

def main(argv):

    pinFile = os.environ["MENUDIR"] + ".kalipi"
    if raw_input('The existing PIN will be overwritten.\nDo you wish to continue (Y/n): ') != 'Y' :
        sys.exit('\nChanges were not recorded\n')

    password = hashlib.sha224(getpass.getpass('Please enter a new PIN: ')).hexdigest()
    try:
        file_conn = open(pinFile,'w')
        file_conn.write(password + '\n')
        file_conn.close()
    except:
        sys.exit('There was a problem saving the PIN!')

    print '\nPIN saved\n'

if __name__ == "__main__":
    main(sys.argv[1:])
