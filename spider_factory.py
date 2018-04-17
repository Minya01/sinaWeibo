from spider.cnbeta import CnbetaParser
from spider.cnblog import CnblogParser
from spider.miaopai import MiaopaParser
# from spider.myBlog import MyBlogParser
from spider.techweb import TechwebParser
from spider.tuicool import TuicoolParser
from spider.toutiao import ToutiaoParser
from spider.wallstreetcn import WallstreetcnParser
from spider.cnr import CnrParser
from spider.cri import CriParser
from spider.yn import YnParser
from spider.taobao import TaobaoParser

spiders = [
    # CriParser(),
    # MyBlogParser(),
    # CnbetaParser(),
    # CnblogParser(),
    # MiaopaParser(),
    # MyBlogParser(),
    # TechwebParser(),
    # TuicoolParser(),
    # ToutiaoParser(),
    # TaobaoParser(),
    # YnParser(),
    CnrParser(),
    WallstreetcnParser(),
]

currentIndex = 0
count = len(spiders)

def nextSpider():
    global currentIndex
    spider = spiders[currentIndex]
    currentIndex = (currentIndex + 1) % count
    return spider
