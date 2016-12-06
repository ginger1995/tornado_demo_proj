#!/usr/bin/env python
# coding=utf-8

import pymysql

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',
                       user='root', passwd='root', db='mysql', charset='utf8')
cur = conn.cursor()
