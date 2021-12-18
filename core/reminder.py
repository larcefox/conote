#!./env/bin/python

"""reminder.py: modual for creating remind message in console."""

__author__ = "Bac9l Xyer"
__copyright__ = "GPLv3"

import subprocess


class Reminder:
    def __new__(cls, *args, **kwargs):
        """Checks that at is installed"""
        find_at = subprocess.run(
            "which at", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL
        )
        if find_at.returncode:
            print('"at" is not installed!')
            exit()

        class_instance = object.__new__(cls)
        return class_instance

    def __init__(self, args: object, template_veriables: dict) -> None:
        self.message = " ".join(args.message)
        self.user = template_veriables["tag_user"]
        self.delay_min = args.run_at[0]
        self.start_at()

    def start_at(self):
        """Exec at and write bash commands with user message at specified delay"""
        at_command = f"""echo "echo {self.message} | write {self.user}" | at now + {self.delay_min} min"""
        subprocess.run(at_command, shell=True, stderr=subprocess.DEVNULL)
