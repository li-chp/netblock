#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File    : demo_view.py
@Time    : 2022/5/23 10:00
@Author  : lichp
@Email   : li-chp@neusoft.com
@Software: PyCharm
"""

from flask import Flask
from view.demo_view import demo
from view.sapi_view import sapi
from scheduler import config

app = Flask(__name__)  # 声明一个Flask实例
app.register_blueprint(demo, url_prefix="/demo")
app.register_blueprint(sapi, url_prefix="/sapi")
config.start(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)