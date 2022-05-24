#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File    : ip_scheduler.py
@Time    : 2022/5/23 17:42
@Author  : lichp
@Email   : li-chp@neusoft.com
@Software: PyCharm
"""
from anguan.driver import anguanDriver
from common.log import logging

LOG = logging.getLogger(__name__)


def getip_task():
    try:
        LOG.info('getip_task')
        anguanDriver().getIp()
    except Exception as e:
        LOG.error(e)
