# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl bleacherreport

class BleacherReportSpider(scrapy.Spider):
    name = 'bleacherreport'
    allowed_domains = ['bleacherreport.com']
    source = 'Bleacher Report'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):
        url = response.url
        datetime = response.css("header .date ::text").extract_first()
        headline = response.css("header h1 ::text").extract_first()
        subhead = ""
        
        author = response.css(".authorInfo .name ::text").extract_first()
       
        bt_lst = response.css(".contentStream p ::text").extract()

        for i in range(len(bt_lst)):
            bt_lst[i] = bt_lst[i].strip()
        body_text = " ".join(bt_lst)

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice


#Twt
#https://bleacherreport.com/articles/2788607-arsenal-transfer-news-hector-herrera-dismisses-porto-exit-rumours