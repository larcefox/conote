#!./env/bin/python

"""write_md.py: modual for creating folder and files."""

__author__      = "Bac9l Xyer"
__copyright__   = "GPLv3"

import os
import datetime

class MakeFile():
    def __init__(self, text, config):
       self.text = text
       self.conote_dir = config['FILE']['conote_dir'] 
       self.conote_file = '/'.join([self.conote_dir, config['FILE']['conote_file']])
       self.current_time = datetime.datetime.now()
       self.template_file = config['FILE']['template_file']
       self.template_event = config['FILE']['template_event']

    @property
    def dir_check(self) -> bool:
        '''Checks existing conote directory, specified in config/config.ini'''
        if os.path.isdir(self.conote_dir):
            return True
        else:
            try:
                os.makedirs(self.conote_dir)
                return True
            except OSError as e:
                print(e)
                return False

    @property
    def file_check(self) -> bool:
        '''Checks existing conote current day file, specified in config/config.ini'''
        if os.path.isfile(self.conote_file):
           print(self.conote_file)
           return True
        else:
            try:
                with open(self.conote_file, 'a') as conote_f:
                    with open(self.template_file, 'r') as template_f:
                        conote_f.write(template_f.read())
                        print(template_f.read())
                return True
            except OSError as e:
                print(e)
                return False

    def file_write(self) -> None:
        '''Write text in file'''
        if self.dir_check and self.file_check:
            try:
                with open(self.conote_file, 'a') as conote_f:
                    with open(self.template_event, 'r') as event_template_f:
                        conote_f.write(event_template_f.read())
                        conote_f.write(''.join(['> ', self.text]))
            except OSError as e:
                print(e)
