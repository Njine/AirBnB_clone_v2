#!/usr/bin/python3
"""Function that deploys"""
from fabric.api import env, local, run
import os

env.hosts = ['35.231.33.237', '34.74.155.163']
env.user = "ubuntu"


def do_clean(number=0):
    """
    Cleans up outdated archives on both local and remote servers.

    Parameters:
    - number (int): The number of archives to keep. Defaults to 0.
    """
    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local_path = 'versions'
    local_command = (
        'cd {} ; ls -t | tail -n +{} | xargs rm -rf'
        .format(local_path, number)
    )
    local(local_command)

    remote_path = '/data/web_static/releases'
    remote_command = (
        'cd {} ; ls -t | tail -n +{} | xargs rm -rf'
        .format(remote_path, number)
    )
    run(remote_command)
