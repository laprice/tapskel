#!/usr/bin/env python

from fabric.api import *
from fabric.contrib.console import confirm

project_name = "tapskel"
deploy_host = "localhost"
project_dir = "/Users/laprice/.virtualenvs/%s/src/" % project_name

env.user = project_name
env.hosts.append(deploy_host)


def test():
    with cd(project_dir):
        run("tests.py")

def install():
    if not env.deploy_dir:
        mkdir(deploy_dir)
    try:
        git_clone(src,deploy_dir)
    except FabricError, e:
        git_pull(src,deploy_dir)
    if not pg_check(db_host, db_user):
        pg_make_db(db_host, db_user, db_init_sql)
    result = pg_check_db(db_host, db_user, sql)
    
