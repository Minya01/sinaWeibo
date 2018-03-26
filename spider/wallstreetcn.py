# -*- coding: utf-8 -*-

# 华尔街见闻

from __future__ import absolute_import
import bs4
from spider.spider import Spider
from weibo.weibo_message import WeiboMessage

HOME_URL = "https://wallstreetcn.com/live/global"


class WallstreetcnParser(Spider):

    def __init__(self):
        super(WallstreetcnParser, self).__init__(HOME_URL)

    def get_weibo_message(self):
        html = self.download_text()
        soup = bs4.BeautifulSoup(html, "html.parser")
        items = soup.find_all(attrs={"class": "content-html"})
        msg = ''
        if len(items) > 0:
            topItem = items[0]
            title = '发一发微博心情倍爽~'
            a = topItem.p.find_all('a')
            if len(a) == 0:
                title = topItem.p.string
            url = ''
            msg = "%s %s" % (title, url)
        return WeiboMessage(msg)
