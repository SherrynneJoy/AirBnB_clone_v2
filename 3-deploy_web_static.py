#!/usr/bin/python3
"""a fafile that creates and distributes an archive to your web servers, using
the function deploy"""
from fabric.api import local, put, run, env
from os.path import isfile
from datetime import datetime


env.hosts = ['54.83.140.28', '54.237.95.53']


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    try:
        date = datetime.utcnow.strftime('%Y%m%d%H%M%S')
        arch_path = 'versions/web_static_{}.tgz'.format(date)
        local('mkdir -p versions')
        local('tar -czvf {} web_static'.format(arch_path))
        return arch_path
    except Exception as e:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not isfile(arch_path):
        return False
    try:
        arch_name = arch_path.split('/')[-1]
        nfile = '/data/web_static/releases/{}'.format(arch_name.split('.')[0])
        put(arch_path, '/tmp/')
        run('mkdir -p {}'.format(nfile))
        run('tar -xzf /tmp/{} -C {}'.format(arch_name, nfile))
        run('rm /tmp/{}'.format(arch_name))
        run('mv {}/web_static/* {}/'.format(nfile, nfile))
        run('rm -rf {}/web_static'.format(nfile))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(nfile))
        return True
    except Exception as e:
        return False


def deploy():
    """creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)


if __name__ == "__main__":
    deploy()
