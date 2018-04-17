# -*- coding: utf-8 -*-

# 华尔街见闻

from __future__ import absolute_import
import bs4
from spider.spider import Spider
from weibo.weibo_message import WeiboMessage

HOME_URL = "http://news.cri.cn/roll"
DOMAIN_URL = "http://news.cri.cn"


class CriParser(Spider):

    def __init__(self):
        super(CriParser, self).__init__(HOME_URL)

    def get_weibo_message(self):
        html = self.download_text()
        soup = bs4.BeautifulSoup(html, "html.parser")
        items = soup.find_all(attrs={"class": "tit"})
        msg = ''
        if len(items) > 0:
            topItem = items[0]
            a = topItem.find('a')
            print(str(a))
            title = a.string
            url = DOMAIN_URL + a.get("href")
            msg = "%s %s" % (title, url)
        return WeiboMessage(msg)
