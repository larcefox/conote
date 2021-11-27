#!./env/bin/python

"""conote.py: Notes your mindes, tasks, todos."""

__author__      = "Bac9l Xyer"
__copyright__   = "GPLv3"

import platform
import argparse
from core.write_md import MakeFile 
import configparser
from datetime import datetime 
import os


config = configparser.ConfigParser()
config.read('./config/config.ini')

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    return uptime_seconds

tag_upt = int(get_uptime())
tag_date = datetime.now().strftime('%y%m%d')
tag_time =  datetime.now().strftime('%H:%M')
tag_sys_name = platform.release() 
tag_user = os.environ['USER']

hour_to_day = 24
sec_to_min = 60
template_tags = {
        config['TAGS']['current_date'] : tag_date,
        config['TAGS']['current_time'] : tag_time,
        config['TAGS']['current_system'] : tag_sys_name, 
        config['TAGS']['uptime'] : ':'.join([
            'd'.join(str(tag_upt // sec_to_min // sec_to_min // hour_to_day)), 
            str(tag_upt // (sec_to_min * sec_to_min) % hour_to_day), 
            str(tag_upt // sec_to_min % sec_to_min), 
            str(tag_upt % sec_to_min)]),
        config['TAGS']['user'] : tag_user}

parser = argparse.ArgumentParser(description='Making notes from consolee')
parser.add_argument('-f', dest='message', action='store_const', 
        const=input("Message:"), 
        help='(Specified that note shoud be saved in .md file.)')

if __name__== '__main__':
    args = parser.parse_args()
    md_file = MakeFile(args.message, config, template_tags) 
    md_file.file_write()
