#!/usr/bin/python3
"""
Deletes out-of-date archives
Usage:
    fab -f 100-clean_web_static.py do_clean:number=2 -i ssh-key -u ubuntu > /dev/null 2>&1
"""

import os
from fabric.api import env, lcd, cd, local, run

env.hosts = ['100.25.130.218', '34.239.253.248']


def do_clean(number=0):
    """
    Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.
                      If 0 or 1, keeps only the most recent archive.
                      If 2, keeps the most and second-most recent archives, etc.
    """
    number = max(1, int(number))

    with lcd("versions"):
        archives_local = sorted(os.listdir("."))
        [local("rm ./{}".format(a)) for a in archives_local[:-number]]

    with cd("/data/web_static/releases"):
        archives_remote = run("ls -tr").split()
        archives_remote = [a for a in archives_remote if "web_static_" in a]
        [run("rm -rf ./{}".format(a)) for a in archives_remote[:-number]]

