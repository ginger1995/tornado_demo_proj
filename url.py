#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website
"""

import sys  # utf-8，兼容汉字
reload(sys)
sys.setdefaultencoding("utf-8")

from handlers.index import IndexHandler
from handlers.search import SearchHandler

url = [
    (r'/', IndexHandler),
    (r'/dictionary', SearchHandler)
]
