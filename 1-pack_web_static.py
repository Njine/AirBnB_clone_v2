#!/usr/bin/python3
# Fabfile to generate a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file_name = "web_static_{}{}{}{}{}{}.tgz".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    file_path = os.path.join("versions", file_name)

    if not os.path.exists("versions"):
        local("mkdir -p versions")

    result = local("tar -cvzf {} web_static".format(file_path))
    if result.failed:
        return None

    return file_path
