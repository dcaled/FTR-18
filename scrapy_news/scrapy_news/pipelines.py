# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import time

class SoccerNewsPipeline(object):
    def open_spider(self, spider):
        self.items = {"news_articles":[]}
        self.source = ''

    def close_spider(self, spider):
        self.file = open('{}_{}.json'.format(time.strftime("%Y_%m_%d"), self.source), 'w', encoding='utf8')
        #self.file = open('{}_{}_41-50.json'.format(time.strftime("%Y_%m_%d"), self.source), 'w', encoding='utf8')
        #self.file = open('{}_thesun.txt'.format(time.strftime("%Y_%m_%d")), 'w', encoding='utf8')

        #json.dump(dict(item), ensure_ascii=False)
        self.file.write(json.dumps(self.items, indent=4, ensure_ascii=False))
        self.file.close()

    def process_item(self, item, spider):
        self.source = item.get('source')

        for attr in item.keys():
            if(item[attr]):
                item[attr] = item[attr].replace("“", '\"')
                item[attr] = item[attr].replace("”", "\"")
                item[attr] = item[attr].replace("‘", "'")
                item[attr] = item[attr].replace("’", "'")
                item[attr] = item[attr].strip()

        self.items["news_articles"].append(dict(item))
        
        return item


