#!/usr/bin/python

"""conote.py: Notes your mindes, tasks, todos."""

__author__      = "Bac9l Xyer"
__copyright__   = "GPLv3"

import argparse
from ctypes import wstring_at

parser = argparse.ArgumentParser(description='Making notes from console.')
parser.add_argument('-f', dest='message', action='store_const', 
        const=input(), 
        help='(Specified that note shoud be saved in .md file.)')



args = parser.parse_args()
print(args)
