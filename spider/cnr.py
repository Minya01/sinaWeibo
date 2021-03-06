# -*- coding: utf-8 -*-

# 华尔街见闻

from __future__ import absolute_import
import bs4
from spider.spider import Spider
from weibo.weibo_message import WeiboMessage

HOME_URL = "https://wallstreetcn.com/news/us"
DOMAIN_URL = "https://wallstreetcn.com"


class CnrParser(Spider):

    def __init__(self):
        super(CnrParser, self).__init__(HOME_URL)

    def get_weibo_message(self):
        html = self.download_text()
        soup = bs4.BeautifulSoup(html, "html.parser")
        items = soup.find_all(attrs={"class": "news-item__main__summary"})
        msg = ''
        if len(items) > 0:
            topItem = items[0]
            title = topItem.string
            url = DOMAIN_URL + topItem.get("href")
            msg = "%s %s" % (title, url)
        return WeiboMessage(msg)
