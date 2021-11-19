
#!/usr/bin/python

"""conote.py: Notes your mindes, tasks, todos."""

__author__      = "Bac9l Xyer"
__copyright__   = "GPLv3"

import os
from date import date


class make_file(text):
    def __init__(self):
       self.text = text 
       self.conote_path = '~/.conote'

    def file_create(self):
        if os.path.exists(self.conote_path):
            pass
        else:
            try:
                os.makedirs(self.conote_path)
            except OSError as e:
                print(e)

    def file_save(self):
        pass

    def file_write(self):
        pass

    
