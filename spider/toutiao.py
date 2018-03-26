# -*- coding: utf-8 -*-

from __future__ import absolute_import
import json
import random
import requests
from spider.spider import Spider
from weibo.weibo_message import WeiboMessage

HOME_URL = "https://www.toutiao.com"
# JSON_URL = "https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1C5AAFB87BA537&cp=5AB7CA7563A7CE1&_signature=rJtonQAA9jvYXRDA9VCgcaybaI"
JSON_URL = "https://www.toutiao.com/api/pc/feed/?category=news_entertainment&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1F52A3B078B229&cp=5AB72B62E2599E1&_signature=WYvhYgAAAzwtTZk.knp8mFmL4X"

# 今日头条
class ToutiaoParser(Spider):

    def __init__(self):
        super(ToutiaoParser, self).__init__(JSON_URL)

    def get_weibo_message(self):
        json_text = self.download_text()
        items = self.getItems(json_text)
        msg = ''
        count = len(items)
        if count > 0:
            index = 1
            msg = items[index]
        return WeiboMessage(msg)

    def getItems(self, jsonStr):
        items = []
        headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }
        response = requests.get(url=JSON_URL,headers=headers)
        nodes = json.loads(response.text)
        results = nodes["data"]
        for node in results:
            url = HOME_URL + node["source_url"]
            msg = node["title"]
            images = ''
            # images = node["middle_image"]
            item = "%s %s" % (msg, url)
            # item = "%s %s %s" % (msg, url, images)
            items.append(item)
        return items

