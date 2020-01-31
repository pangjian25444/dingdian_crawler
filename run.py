# author: pangjian
# time: 2019/12/10 12:20
# software: PyCharm

from dingdian.spiders.dingdian import DingDianSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
process = CrawlerProcess(settings=settings)

process.crawl(DingDianSpider)
process.start()
