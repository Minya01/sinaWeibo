# -*- coding: utf-8 -*-

from __future__ import absolute_import
import json
import random
import requests
from spider.spider import Spider
from weibo.weibo_message import WeiboMessage

HOME_URL = "http://127.0.0.1/test/data/test.json"

# 淘宝
class TaobaoParser(Spider):

    def __init__(self):
        super(TaobaoParser, self).__init__(HOME_URL)

    def get_weibo_message(self):
        json_text = self.download_text()
        items = self.getItems(json_text)
        msg = ''
        count = len(items)
        images = []
        if count > 0:
            # index = random.randint(0, count - 1)
            index = 0
            msg = items[index]
            images.append(self.images[index])
        return WeiboMessage(msg,images)

    def getItems(self, jsonStr):
        items = []
        headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }
        response = requests.get(url=HOME_URL,headers=headers)
        results = json.loads(response.text)
        self.images = []
        for node in results:
            url = ''
            # if node['couponURL']:
                # url = node['couponURL']
            msg = node["title2"]
            image = node["image"]
            self.images.append(image)
            item = "%s %s" % (msg, url)
            items.append(item)
        return items

