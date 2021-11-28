#!/home/larce/projects/conote/env/bin/python

"""conote.py: Notes your mindes, tasks, todos."""

__author__      = "Bac9l Xyer"
__copyright__   = "GPLv3"

import platform
import argparse
from core.write_md import MakeFile 
import configparser
from datetime import datetime 
import os
import subprocess


path = os.path.abspath('.')
config = configparser.ConfigParser()
config.read("".join([path, '/config/config.ini']))

# ====================TAGS===================================================

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    return uptime_seconds

tag_upt = int(get_uptime())
tag_date = datetime.now().strftime('%y%m%d')
tag_time =  datetime.now().strftime('%H:%M')
tag_sys_name = platform.node()
tag_user = os.environ['USER']

hour_to_day = 24
sec_to_min = 60
template_tags = {
        config['TAGS']['current_date'] : tag_date,
        config['TAGS']['current_time'] : tag_time,
        config['TAGS']['current_system'] : tag_sys_name, 
        config['TAGS']['uptime'] : ':'.join([
            str(tag_upt // sec_to_min // sec_to_min // hour_to_day), 
            str(tag_upt // (sec_to_min * sec_to_min) % hour_to_day), 
            str(tag_upt // sec_to_min % sec_to_min), 
            str(tag_upt % sec_to_min)]),
        config['TAGS']['user'] : tag_user}


# ====================TAGS===================================================

parser = argparse.ArgumentParser(description='Making notes from consolee')
parser.add_argument('message', type=str, nargs='+',
        help='(Specified that note shoud be saved in .md file.)')
parser.add_argument('-r', '--remind', dest='run_at', action='store_true',
        help='(Show message to you at specified time.)')

args = parser.parse_args()
space_str = ' '
at_command = 'echo "echo {space_str.join(args.message)} \
        | write {tag_user}" | at now + 1 min'


if __name__== '__main__':
    print(" ".join(args.message))
    args.run_at and subprocess.run(at_command, shell=True) 

    md_file = MakeFile(" ".join(args.message), config, template_tags) 
    md_file.file_write()
