#!/usr/bin/env python

"""

a simple script that calculates the import hash of a Windows executable file

"""

import sys
import pefile

usage = (
"\nUsage: imphashcalc.py filename.exe\n"
)

if len(sys.argv) < 2:
    print usage
    sys.exit(0)

pe = pefile.PE(sys.argv[1])
exe = sys.argv[1]
imphash = pe.get_imphash()

print '[*] File: ' + exe + ' ImpHash: '+ imphash 



