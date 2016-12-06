#!/usr/bin/env python
# coding=utf-8

from db import *


def select_table(table, column, condition, value):
    lines=()
    sql = "select " + column + " from " + table + \
        " where " + condition + "='\\\'" + value + "\\\''"
    print sql
    cur.execute(sql)
    lines = cur.fetchall()
    return lines
