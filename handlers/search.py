#!/usr/bin/env python
# coding=utf-8

import tornado.web
import methods.readdb as mrd


class SearchHandler(tornado.web.RequestHandler):

    def get(self):
        word = self.get_argument("word")
        word_item = mrd.select_table(
            table="wordbank", column="*", condition="word", value=word)
        self.render("word.html", worditem=word_item)
