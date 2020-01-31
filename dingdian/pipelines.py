# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class DingdianDataClearPipeline(object):
    def process_item(self, item, spider):
        item['book_name'] = item['book_name'].strip().replace(' 全文阅读', '')
        item['book_words'] = item['book_words'].strip().replace('字', '')
        item['book_anthor'] = item['book_anthor'].strip()
        item['book_status'] = item['book_status'].strip()
        item['book_type'] = item['book_type'].strip()
        item['book_time'] = item['book_time'].strip()
        item['book_click_nums'] = item['book_click_nums'].strip()
        return item


class DingdianPipeline(object):
    def process_item(self, item, spider):
        return item
