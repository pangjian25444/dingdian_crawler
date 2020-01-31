# author: pangjian
# time: 2019/12/8 20:49
# software: PyCharm

import scrapy
import re

from dingdian.items import DingdianItem


class DingDianSpider(scrapy.Spider):
    name = 'dingdian'

    # start_urls = ['https://www.ddxsku.com']

    def __init__(self, name=None, **kwargs):
        super().__init__(name=None, **kwargs)
        self.parse_list = None

    def start_requests(self):
        yield scrapy.Request('https://www.23us.so', callback=self.parse)

    def parse(self, response):
        # /html/body/div[2]//*[@id="centeri"]/div/div[2]/ul
        urls = response.xpath('//div[@class="main m_menu"]/ul/li/a/@href').extract()
        urls = urls[1: -2]
        for url in urls:
            # yield scrapy.Request('https://www.ddxsku.com/' + url, callback=self.parse_lists)
            yield response.follow(url, callback=self.get_page_nums)

    def get_page_nums(self, response):
        text = response.text
        page_nums = re.search(r'class="last">(.*?)</a>', text).group(1)
        page_nums = int(page_nums)

        url = response.url

        for i in range(1, page_nums + 1):
            new_url = re.sub(r'_\d+', '_' + str(i), url)
            yield scrapy.Request(new_url, callback=self.parse_lists, dont_filter=True)

    def parse_lists(self, response):
        urls = response.xpath('//tr[@bgcolor="#FFFFFF"]/td[1]/a/@href').extract()

        for url in urls:
            yield scrapy.Request(url, callback=self.parse_details)

    def parse_details(self, response):
        book_name = response.xpath('//h1/text()').extract_first()
        book_anthor = response.xpath('//table[@id="at"]/tr[1]/td[2]/text()').extract_first()
        book_type = response.xpath('//table[@id="at"]/tr[1]/td[1]/a/text()').extract_first()
        book_status = response.xpath('//table[@id="at"]/tr[1]/td[3]/text()').extract_first()
        book_words = response.xpath('//table[@id="at"]/tr[2]/td[2]/text()').extract_first()
        book_time = response.xpath('//table[@id="at"]/tr[2]/td[3]/text()').extract_first()
        book_click_nums = response.xpath('//table[@id="at"]/tr[3]/td[1]/text()').extract_first()

        item = DingdianItem()
        item['book_name'] = book_name
        item['book_anthor'] = book_anthor
        item['book_status'] = book_status
        item['book_type'] = book_type
        item['book_words'] = book_words
        item['book_time'] = book_time
        item['book_click_nums'] = book_click_nums

        yield item
