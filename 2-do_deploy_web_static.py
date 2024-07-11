#!/usr/bin/python3
"""
Empaqueter le contenu statique et le déployer sur le serveur.
"""
import time
from fabric.api import local, put, run, env
import os.path

env.hosts = ["100.27.4.173", "34.201.161.76"]
env.user = 'ubuntu'

def do_pack():
    """
    Empaqueter le contenu statique.
    """
    try:
        directory_name = 'versions'
        if not os.path.exists(directory_name):
            local("mkdir -p {}".format(directory_name))
        timestamp = time.strftime("%Y%m%d%H%M%S", time.gmtime())
        file_name = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Une erreur est survenue: {}".format(e))
        return None


def do_deploy(archive_path):
    """
    Déployer mon archive tgz sur mes serveurs.
    """
    if not os.path.isfile(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]

        remote_path = "/data/web_static/releases"
        tmp_archive = "/tmp/{}".format(file_name)
        target_path = "{}/{}".format(remote_path, base_name)

        put(archive_path, tmp_archive)
        run('mkdir -p {}/'.format(target_path))
        run('tar -xzf {} -C {}/'.format(tmp_archive, target_path))
        run('rm {}'.format(tmp_archive))
        run('mv {0}/web_static/* {0}/'.format(target_path))
        run('rm -rf {}/web_static'.format(target_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(target_path))
        return True
    except Exception as e:
        print("Déploiement échoué: {}".format(e))
        return False


def deploy():
    """
    Empaqueter et déployer.
    """
    archive_path = do_pack()
    if archive_path:
        return do_deploy(archive_path)
    else:
        return False
