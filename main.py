#!/home/larce/projects/conote/env/bin/python

"""conote.py: Notes your mindes, tasks, todos."""

__author__ = "Bac9l Xyer"
__copyright__ = "GPLv3"

import argparse
import configparser
import os
import platform
import select
import sys
from datetime import datetime
from loguru import logger

from pathlib import Path
from core.reminder import Reminder
from core.write_md import MakeFile
from core.write_theme_md import MakeThemeFile

"""Config load"""
path = Path(__file__).parent.absolute()
config = configparser.ConfigParser()
config.read(path / "config/config.ini")

# ====================TAGS===================================================


def get_uptime():
    with open("/proc/uptime", "r") as f:
        uptime_seconds = float(f.readline().split()[0])
    return uptime_seconds


template_veriables = {
    "tag_upt": int(get_uptime()),
    "tag_date": datetime.now().strftime("%y%m%d"),
    "tag_time": datetime.now().strftime("%H:%M"),
    "tag_sys_name": platform.node(),
    "tag_user": os.environ["USER"],
}

hour_to_day = 24
sec_to_min = 60
template_tags = {
    config["TAGS"]["current_date"]: template_veriables["tag_date"],
    config["TAGS"]["current_time"]: template_veriables["tag_time"],
    config["TAGS"]["current_system"]: template_veriables["tag_sys_name"],
    config["TAGS"]["uptime"]: ":".join(
        [
            str(
                template_veriables["tag_upt"] // sec_to_min // sec_to_min // hour_to_day
            ),
            str(
                template_veriables["tag_upt"] // (sec_to_min * sec_to_min) % hour_to_day
            ),
            str(template_veriables["tag_upt"] // sec_to_min % sec_to_min),
            str(template_veriables["tag_upt"] % sec_to_min),
        ]
    ),
    config["TAGS"]["user"]: template_veriables["tag_user"],
}

# ====================TAGS===================================================


parser = argparse.ArgumentParser(description="Making notes from consolee")

# redirect input from pipe to argparser
if select.select(
    [
        sys.stdin,
    ],
    [],
    [],
    0.0,
)[0]:
    sys.argv.append(sys.stdin.read())

parser.add_argument(
    "message",
    type=str,
    nargs="+",
    help="(Specified that note shoud be saved in .md file.)",
)

parser.add_argument(
    "-r",
    "--remind",
    dest="run_at",
    type=int,
    nargs=1,
    help="(Show message to you at specified time.)",
)
parser.add_argument(
    "-t",
    "--theme",
    dest="theme_file",
    type=str,
    nargs="+",
    help="(Show message to you at specified time.)",
)
args = parser.parse_args()

if __name__ == "__main__":

    user_meassage = " ".join(args.message)
    md_file = MakeFile(user_meassage, config, template_tags, path)
    md_file.file_write()

    if args.theme_file:
        user_theme_file = "".join(args.theme_file)
        theme_file_md = MakeThemeFile(
            user_meassage, config, template_tags, user_theme_file, path
        )
        theme_file_md.file_write()

    if args.run_at:
        reminder = Reminder(args, template_veriables)
