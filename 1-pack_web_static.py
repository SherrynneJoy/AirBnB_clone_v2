#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """used to generate a tgz"""
    local("sudo mkdir -p versions")
    date = datetime.now()
    timestamp = date.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    res = local("tar -czvf {} web_static".format(archive_name))
    if res.succeeded:
        return archive_name
    else:
        None
