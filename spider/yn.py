# -*- coding: utf-8 -*-

# 一牛财经

from __future__ import absolute_import
import json
import random
import requests
from spider.spider import Spider
from weibo.weibo_message import WeiboMessage

HOME_URL = "https://api-prod.wallstreetcn.com/apiv1/content/lives?channel=tech-channel&client=pc&limit=3"


class YnParser(Spider):

    def __init__(self):
        super(YnParser, self).__init__(HOME_URL)

    def get_weibo_message(self):
        headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }
        response = requests.get(url=HOME_URL,headers=headers)
        nodes = json.loads(response.text)
        results = nodes["data"]["items"]
        msg = ''
        print(len(results))
        if len(results) > 1:
            topItem = results[1]
            title = topItem["content_text"]
            print(title)
            url = ''
            msg = "%s %s" % (title, url)
        return WeiboMessage(msg)
