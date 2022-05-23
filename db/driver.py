#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File    : driver.py
@Time    : 2022/5/23 17:25
@Author  : lichp
@Email   : li-chp@neusoft.com
@Software: PyCharm
"""

import pymysql
import yaml

def getConnect():
    try:
        with open('config.yml', 'r') as f:
            result = yaml.load(f, Loader=yaml.FullLoader)
            mysqlresult = result['mysql']
        connect = pymysql.connect(mysqlresult['host'], mysqlresult['username'], mysqlresult['password'], mysqlresult['database'], mysqlresult['port'])
        return connect
    except Exception as e:
        print( e )

def selectByParameters( sql, params = None ):
    try:
        connect = getConnect()
        cursor = connect.cursor( pymysql.cursors.DictCursor )
        cursor.execute( sql, params )
        result = cursor.fetchall()
        return result
    except Exception as e:
        print( e )
    finally:
        try:
            cursor.close()
        except Exception as e:
            print(e)
        try:
            connect.close()
        except Exception as e:
            print(e)

def updateByParameters( sql, params = None ):
    try:
        connect = getConnect()
        cursor = connect.cursor( pymysql.cursors.DictCursor )
        count = cursor.execute( sql, params )
        connect.commit()
        return count
    except Exception as e:

        connect.rollback()
        print( e )
    finally:
        try:
            cursor.close()
        except Exception as e:
            print(e)
        try:
            connect.close()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    sql = "insert into request_log_t(url, req, resp, status, create_time) values (%s, %s, %s, %s, now())"
    result = updateByParameters(sql, params=('aa', 'bb', 'cc', '200'))
    print( result )