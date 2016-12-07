#!/usr/bin/env python
# coding=utf-8

import tornado.web
import methods.readdb as mrd


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")

    # IndexHandler中的post方法对应着处理index.html中的post方式的请求
    def post(self):
        # 先通过get_argument()方法活得前端index.html传过来的参数word的值，再根据这个值去数据库查询
        word = self.get_argument("word")
        word_item = mrd.select_table(
            table='wordbank', column='*', condition='word', value=word)
        if word_item == ():
            # 若根据word的值查询到不为空再向前端由write()方法传回该word的值，由前端的ajax函数去处理进一步的请求
            self.write("nodata")
        else:
            self.write(word)
