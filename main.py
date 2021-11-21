#!./env/bin/python

"""conote.py: Notes your mindes, tasks, todos."""

__author__      = "Bac9l Xyer"
__copyright__   = "GPLv3"

import argparse
from core.write_md import MakeFile 
import configparser


config = configparser.ConfigParser()
config.read('./config/config.ini')

parser = argparse.ArgumentParser(description='Making notes from console.')
parser.add_argument('-f', dest='message', action='store_const', 
        const=input(), 
        help='(Specified that note shoud be saved in .md file.)')

if __name__== '__main__':
    args = parser.parse_args()
    print(args)
    md_file = MakeFile(args.message, config) 
    md_file.file_write()
