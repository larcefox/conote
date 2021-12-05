
#!./env/bin/python

"""reminder.py: modual for creating remind message in console."""

__author__      = "Bac9l Xyer"
__copyright__   = "GPLv3"

import subprocess


class Reminder():
    def __init__(self, args, template_veriables):
        self.message = ' '.join(args.message)
        self.user = template_veriables['tag_user']
        self.delay_min = args.run_at[0]
        
    def start_at(self):
        '''Exec at and write bash commands with user message at specified delay'''
        at_command = \
        f"""echo "echo {self.message} | write {self.user}" | at now + {self.delay_min} min"""
        subprocess.run(
                at_command, shell=True,
                stderr=subprocess.DEVNULL)

    def at_check(self):
        try:
            where_at = subprocess.check_output('where att', shell=True)                       
            return True
        except subprocess.CalledProcessError as grepexc:                                                                                                   
            print("Error 'at' install required")
            return False
