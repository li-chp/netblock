#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File    : db.py
@Time    : 2022/5/23 14:10
@Author  : lichp
@Email   : li-chp@neusoft.com
@Software: PyCharm
"""

from common import db
from common.log import logging
import json
import requests
import yaml

LOG = logging.getLogger(__name__)
HEADERS = {'content-type': 'application/json;charset=utf-8'}

def http_request(method, url, **kwargs):
    resp = requests.request(method, url, **kwargs)
    sql = "insert into request_log_t(url, req, resp, status, create_time) values (%s, %s, %s, %s, now())"
    db.updateByParameters(sql, params=(url, json.dumps(kwargs['data']), json.dumps(json.loads(resp.content)), resp.status_code))


class anguanDriver():

    def __init__(self):
        with open('config.yml', 'r') as f:
            result = yaml.load(f, Loader=yaml.FullLoader)
            ag = result['anguan_platform']
        self.http_url = ag['http_url']
        self.org_id = ag['org_id']

    def getIp(self):
        path = "/getip"
        body = {
            "orgid": self.org_id
        }
        http_request('POST', self.http_url + path, data=body, headers=HEADERS)

    def sync(self):
        path = "/sync"
        body = {
            "orgid": self.org_id,
            "data":	{
                "closeip": [{
                    "ip": "39.56.13.177",
                    "result": "1"
                    }, {
                        "ip": "19.333.14.1/24",
                        "result": "0"
                    },
                    {
                        "ip": "39.156.34.100-39.156.34.200",
                        "result": "1"
                    }
                ],
                "openip": [{
                    "ip": "39.39.39.39",
                    "result": "1"
                }, {
                    "ip": "38.56.39.56",
                    "result": "1"
                }]
            }
        }
        requests.post(self.http_url, data=body, headers=HEADERS)

