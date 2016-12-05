#!/usr/bin/env python
# coding=utf-8
'''
这个文件完成了对网站系统的基本配置，建立网站的请求处理集合。
'''
from url import url

import tornado.web
import os
# settings约定了已经建立的文件夹templates和statics的路径
settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "statics")
)
# 请求处理集合对象
application = tornado.web.Application(
    handlers=url,
    **settings
)
