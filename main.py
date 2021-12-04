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
import sys
import select


path = os.path.abspath('.')
config = configparser.ConfigParser()
config.read("".join([path, '/config/config.ini']))

# ====================TAGS===================================================

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    return uptime_seconds

template_veribls = {
    'tag_upt' : int(get_uptime()),
    'tag_date' : datetime.now().strftime('%y%m%d'),
    'tag_time' :  datetime.now().strftime('%H:%M'),
    'tag_sys_name' : platform.node(),
    'tag_user' : os.environ['USER']}

hour_to_day = 24
sec_to_min = 60
template_tags = {
        config['TAGS']['current_date'] : template_veribls['tag_date'],
        config['TAGS']['current_time'] : template_veribls['tag_time'],
        config['TAGS']['current_system'] : template_veribls['tag_sys_name'], 
        config['TAGS']['uptime'] : ':'.join([
            str(template_veribls['tag_upt'] // sec_to_min // sec_to_min // hour_to_day), 
            str(template_veribls['tag_upt'] // (sec_to_min * sec_to_min) % hour_to_day), 
            str(template_veribls['tag_upt'] // sec_to_min % sec_to_min), 
            str(template_veribls['tag_upt'] % sec_to_min)]),
        config['TAGS']['user'] : template_veribls['tag_user']}


# ====================TAGS===================================================

if select.select([sys.stdin,], [], [], 0.0)[0]: 
    sys.argv.append(sys.stdin.read())

parser = argparse.ArgumentParser(description='Making notes from consolee')
parser.add_argument('message', type=str, nargs='+',
        help='(Specified that note shoud be saved in .md file.)')
parser.add_argument('-r', '--remind', dest='run_at', type=int, 
        nargs=1, 
        help='(Show message to you at specified time.)')
args = parser.parse_args()

if args.run_at:
    space_str = ' '
    at_command = \
    f"""echo "echo {space_str.join(args.message)} | write {template_veribls['tag_user']}" | at now + {args.run_at[0]} min"""
    subprocess.run(
            at_command, shell=True,
            stderr=subprocess.DEVNULL) 


if __name__== '__main__':

    md_file = MakeFile(" ".join(args.message), config, template_tags) 
    md_file.file_write()
