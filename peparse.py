#!/usr/bin/env python

"""

a simple script that parses a Windows executable file for observable metadata of interest

"""

import sys
import pefile
import time
import peutils

usage = (
"\nUsage: peparse.py filename.exe\n"
)

if len(sys.argv) < 2:
    print usage
    sys.exit(0)

pe = pefile.PE(sys.argv[1])
exe = sys.argv[1]
imphash = pe.get_imphash()
entrypoint = hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint)
sections = pe.FILE_HEADER.NumberOfSections
epoch = pe.FILE_HEADER.TimeDateStamp
humantime = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(epoch))
subsystem = pefile.SUBSYSTEM_TYPE[pe.OPTIONAL_HEADER.Subsystem]
machine = pefile.MACHINE_TYPE[pe.FILE_HEADER.Machine] 
signatures = peutils.SignatureDatabase('/opt/PEiD/UserDB.TXT')
matches = signatures.match_all(pe,ep_only = True)

print '[*] File: ' + exe + ' imphash: '+str(imphash)+', Entry Point: '+str(entrypoint)+', Compile Time: '+str(machine)

print matches



