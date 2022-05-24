#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File    : demo_scheduler.py
@Time    : 2022/5/23 11:13
@Author  : lichp
@Email   : li-chp@neusoft.com
@Software: PyCharm
"""
from common.log import logging
import datetime

LOG = logging.getLogger(__name__)

def task(a, b):
    LOG.info(str(datetime.datetime.now()) + ' execute task ' + '{}+{}={}'.format(a, b, a + b))