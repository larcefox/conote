
#!./env/bin/python

"""reminder.py: modual for creating remind message in console."""

__author__      = "Bac9l Xyer"
__copyright__   = "GPLv3"

import os
import datetime

class Reminder():
    def __init__(self, message, template_veribls):
        space_str = ' '
        at_command = \
        f"""echo "echo {space_str.join(args.message)} | write {template_veribls['tag_user']}" | at now + {args.run_at[0]} min"""
