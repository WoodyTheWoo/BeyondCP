# -*- coding: utf-8 -*-

"""
    ~~ BeyondCP - scheduler.py ~~

@author         WoodyTheWoo
@licence        2014
@version        v 0.1
"""

from apscheduler.scheduler import Scheduler

# Start the scheduler
sched = Scheduler()
sched.start()


def job_function():
    print("Hello World !")


sched.add_interval_job(job_function, seconds=10)

