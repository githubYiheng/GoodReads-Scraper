# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter, JsonItemExporter

class GoodreadsScraperPipeline(object):
    def __init__(self):
        self.file = open('all_quotes' + '.json', 'a+b')
        # self.exporter = JsonLinesItemExporter(self.file)
        self.exporter = JsonItemExporter(self.file)

    def spider_opened(self, spider):
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
         self.exporter.export_item(item)
