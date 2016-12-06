#!/usr/bin/env python
# coding=utf-8

import tornado.web
import methods.readdb as mrd


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")

    def post(self):
        word = self.get_argument("word")
        word_item = mrd.select_table(
            table='wordbank', column='*', condition='word', value="\\\'"+word+"\\\'")
        if word_item == ():
            self.write("nodata")
        else:
            self.write("\\\'happy\\\'")
