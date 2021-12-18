#!./env/bin/python

"""write_theme_md.py: modual for creating themed note files."""

__author__ = "Bac9l Xyer"
__copyright__ = "GPLv3"

import os
import datetime


class MakeThemeFile:
    def __init__(self, text: str, config, template_tags, theme_file, path):
        self.template_tags = template_tags
        self.text = text
        self.config = config
        self.conote_dir = self.config["FILE"]["conote_dir"]
        self.conote_file = "/".join([self.conote_dir, "".join([theme_file, ".md"])])
        self.date_time = datetime.datetime.now()
        self.template_file = path / self.config["FILE"]["template_theme_file"]
        self.template_event = path / self.config["FILE"]["template_theme_event"]
        self.md_new_line_simbol = self.config["MD_NEWLINE"]["simbol"]

    @property
    def dir_check(self) -> bool:
        """Checks existing conote directory, specified in config/config.ini"""
        # breakpoint()
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
        """Checks existing conote current day file, specified in config/config.ini"""
        if os.path.isfile(self.conote_file):
            return True
        else:
            try:
                with open(self.conote_file, "w") as conote_f:
                    with open(self.template_file, "r") as template_f:
                        header = template_f.read()
                        conote_f.write(header)
            except OSError as e:
                print(e)
                return False
            return True

    def tag_replace(self, event_template_text):
        """Place varibls insted tags in template"""
        for tag in self.template_tags:
            if tag in event_template_text:
                event_template_text = event_template_text.replace(
                    tag, str(self.template_tags[tag])
                )
        return event_template_text

    def file_write(self) -> None:
        """Write messagei in file"""
        if self.dir_check and self.file_check:
            try:
                with open(self.conote_file, "a") as conote_f:
                    with open(self.template_event, "r") as event_template_f:
                        templ_text = self.tag_replace(event_template_f.read())
                        text_list = "".join([self.text]).split("\n")
                        conote_f.write(templ_text)
                        [
                            conote_f.write(
                                "".join([self.md_new_line_simbol, line, "\n"])
                            )
                            for line in text_list
                        ]
            except OSError as e:
                print(e)
