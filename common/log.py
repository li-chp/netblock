#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File    : log.py
@Time    : 2022/5/24 19:01
@Author  : lichp
@Email   : li-chp@neusoft.com
@Software: PyCharm
"""

import logging

log_file = '../netblock.log'

# 创建日志器  这个日志器就写入了日志信息
logger = logging.getLogger()
# 显示日志信息全面 设置日志级别
logger.setLevel(logging.DEBUG)
# 需要控制台处理器
sh = logging.StreamHandler()
# 日志信息放入控制台中
logger.addHandler(sh)

# 保存在文件中 文件处理器
fh = logging.FileHandler(log_file)
# 把日志信息添加到文件中去
logger.addHandler(fh)

# 日志比较丑，设置格式  创建格式器
fmt = '%(asctime)s %(levelname)s %(pathname)s %(message)s'
formater = logging.Formatter(fmt)

# 给控制台加格式
sh.setFormatter(formater)
# 给日志文件处理器加格式
fh.setFormatter(formater)
