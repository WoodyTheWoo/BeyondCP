# -*- coding: utf-8 -*-

"""
    ~~ BeyondCP - run.py ~~

@author         WoodyTheWoo
@licence        2014
@version        v 0.1
"""

from os.path import exists

from apscheduler.scheduler import Scheduler

from app import run
from database import db_create_table, DATABASE_PATH


if __name__ == "__main__":
    if exists(DATABASE_PATH):
        print("Database OK")
    else:
        print("Database KO")
        db_create_table()

    sched = Scheduler()
    # sched.add_interval_job(hello, seconds=1)

    sched.start()
    run(host='0.0.0.0', debug=True)