#!/usr/bin/python3
'''fabfile tar packaging'''
from fabric.api import local, run, prefix, env
from datetime import datetime
import os

env.hosts = ['localhost']


def do_pack():
    '''
    Generates a .tgz archive from web_static folder
    '''
    try:
        n = datetime.now()
        name = "web_static_{}{}{}{}{}{}.tgz".format(n.year, n.month,
                                                    n.day, n.hour,
                                                    n.minute, n.second)
        local('mkdir -p versions')
        local("tar -cvzf versions/{} web_static".format(name))
        size = os.stat("versions/{}".format(name)).st_size
        print("web_static packed: versions/{} -> {}".format(name, size))
    except:
        return None
