#!/usr/bin/env python


# At this stage, this is more of a todo list.
# need to get up to speed on fabric.
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
    
