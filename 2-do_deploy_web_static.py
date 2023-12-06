#!/usr/bin/python3
"""a Fabric script that distributes an archive to your web servers, using the
function do_deploy"""
from fabric.api import *
from datetime import datetime
from os.path import exists


"""remote commands executed both servers"""
env.hosts = ['54.83.140.28', '54.237.95.53']


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if exists(archive_path) is False:
        return False
    file_name = archive_path.split('/')[-1]
    nfile = '/data/web_static/releases/' + "{}".format(file_name.split('.')[0])
    tmp = "/tmp/" + file_name

    try:
        """Upload the archive to the /tmp/ directory of the web server"""
        put(archive_path, "/tmp/")
        """Uncompress the archive to the folder /data/web_static/releases/
        <archive filename without extension> on the web server"""
        run("mkdir -p {}/".format(nfile))
        run("tar -xzf {}  -C {}/".format(tmp, nfile))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(nfile, nfile))
        """Delete the archive from the web server"""
        run("rm -rf {}/web_static".format(nfile))
        """Delete the symbolic link from the web server"""
        run("rm -rf /data/web_static/current")
        """Create a new the symbolic link"""
        run("ln -s {}/ /data/web_static/current".format(nfile))
        return True
    except Exception as e:
        print("Exception:", e)
        return False
