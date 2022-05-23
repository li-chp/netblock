#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File    : ip_scheduler.py
@Time    : 2022/5/23 17:42
@Author  : lichp
@Email   : li-chp@neusoft.com
@Software: PyCharm
"""
from db import driver as db_driver
from anguan.driver import anguanDriver

def getip_task():
    try:
        anguanDriver().getIp()
    except Exception as e:
        print e
