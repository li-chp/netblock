#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2022/5/23 10:55
@Author  : lichp
@Email   : li-chp@neusoft.com
@Software: PyCharm
"""

from flask import Blueprint
from flask import render_template
import json

sapi = Blueprint("sapi", __name__)

@sapi.route('/getip', methods=['POST'])
def getip():

    resp = {
        "code":"0",
        "msg":"20220202153015",
        "data": {
            "closeip": ["39.56.13.177",
                "19.333.14.1/24",
                "39.156.34.100-39.156.34.200"
            ],
            "openip": ["39.39.39.39", "38.56.39.1/24"]
        }
    }
    return resp

@sapi.route('/sync', methods=['POST'])
def sync():
    resp = {
        "code": "0",
        "msg": "请求成功"
    }
    return resp
