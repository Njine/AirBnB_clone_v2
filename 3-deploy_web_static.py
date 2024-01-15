from fabric.api import put, run, env
from os.path import exists

env.hosts = ['100.25.130.218', '34.239.253.248']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distribute an archive to the web servers."""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        no_extension = file_name.split(".")[0]
        path = "/data/web_static/releases/"

        # Upload the archive
        put(archive_path, '/tmp/')

        # Create release directory
        run('mkdir -p {}{}/'.format(path, no_extension))

        # Extract the archive
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_extension))

        # Remove the uploaded archive
        run('rm /tmp/{}'.format(file_name))

        # Move contents to the release directory
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_extension))

        # Remove the web_static directory
        run('rm -rf {}{}/web_static'.format(path, no_extension))

        # Update the symbolic link
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_extension))

        return True
    except Exception as e:
        print(e)
        return False
