#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File    : config.py
@Time    : 2022/5/23 11:12
@Author  : lichp
@Email   : li-chp@neusoft.com
@Software: PyCharm
"""
from common.log import logging
from flask_apscheduler import APScheduler

LOG = logging.getLogger(__name__)


class Config(object):
    JOBS = [
        # {
        #     'id': 'demo_job1',
        #     'func': 'scheduler.demo_scheduler:task',
        #     'args': (1, 2),
        #     'trigger': 'interval',
        #     'seconds': 10
        # },

        {
            'id': 'getip_job',
            'func': 'scheduler.ip_scheduler:getip_task',
            # 'args': None,
            'trigger': 'interval',
            'seconds': 10
        }
    ]
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    SCHEDULER_API_ENABLED = True

def start(app):
    app.config.from_object(Config())
    scheduler = APScheduler()
    scheduler.init_app(app)
    LOG.info("启动定时任务调度器。。。")
    scheduler.start()
