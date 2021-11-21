#!./env/bin/python

"""write_md.py: modual for creating folder and files."""

__author__      = "Bac9l Xyer"
__copyright__   = "GPLv3"

import os
import datetime

class MakeFile():
    def __init__(self, text, config):
       self.text = text
       self.config = config
       self.conote_dir = self.config['FILE']['conote_dir'] 
       self.conote_file = '/'.join([self.conote_dir, self.config['FILE']['conote_file']])
       self.date_time = datetime.datetime.now()
       self.template_file = self.config['FILE']['template_file']
       self.template_event = self.config['FILE']['template_event']

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
           return True
        else:
            try:
                # breakpoint()
                with open(self.conote_file, 'w') as conote_f:
                    with open(self.template_file, 'r') as template_f:
                        header = template_f.read()
                        conote_f.write(header)
            except OSError as e:
                print(e)
                return False
            return True

    # def tag_dict(self):
        # for line in str(os.system('lsb_release -a')):
            # if 'Description:' in line:
                # dist = line.split()[1]
                # print(dist)
    # TODO Need to create template tags interpretation
    def file_write(self) -> None:
        '''Write text in file'''
        # breakpoint()
        if self.dir_check and self.file_check:
            try:
                with open(self.conote_file, 'a') as conote_f:
                    with open(self.template_event, 'r') as event_template_f:
                        conote_f.write(event_template_f.read())
                        self.tag_dict()
                        conote_f.write(''.join(['> ', self.text]))
            except OSError as e:
                print(e)
