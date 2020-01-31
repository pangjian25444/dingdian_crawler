# author: pangjian
# time: 2019/12/10 12:18
# software: PyCharm

from scrapy.cmdline import execute
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "dingdian"])
