# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class BookParserPipeline:
    def __init__(self):
        client = MongoClient('127.0.0.1', 27017)
        self.db = client['hw_books']

    def process_item(self, item, spider):
        colection = self.db[spider.name]
        colection.insert_one(item)
        return item
