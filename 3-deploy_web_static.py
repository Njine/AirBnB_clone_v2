#!/usr/bin/python3
"""Create and distribute an archive to web servers"""
import os.path
import time
from fabric.api import local, put, run, env

env.hosts = ['100.25.130.218', '34.239.253.248']


def create_archive():
    """Generate a tgz archive from web_static folder"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return "versions/web_static_{}.tgz".format(
            time.strftime("%Y%m%d%H%M%S")
        )
    except Exception as e:
        print(f"Error creating archive: {e}")
        return None


def do_deploy(archive_path):
    """Distribute an archive to web servers"""
    if not os.path.isfile(archive_path):
        return False

    try:
        file_name = os.path.basename(archive_path)
        folder = "/data/web_static/releases/{}".format(
            file_name.split(".")[0]
        )
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder))
        print("Deployment done")
        return True
    except Exception as e:
        print(f"Error deploying archive: {e}")
        return False


def deploy():
    """Create and distribute an archive to web servers"""
    try:
        path = create_archive()
        return do_deploy(path)
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
