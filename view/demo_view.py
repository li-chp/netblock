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

demo = Blueprint("demo", __name__)

@demo.route('/', methods=['GET'])
def test():
    # 往模板中传入的数据
    my_int = 18
    my_str = 'hello world'
    my_list = [1, 5, 4, 3, 2]
    my_dict = {
        'name': 'xiaoming',
        'age': 18
    }
    return render_template('demo.html',
                           my_str=my_str,
                           my_int=my_int,
                           my_list=my_list,
                           my_dict=my_dict
                           )
