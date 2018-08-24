# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl hitc

class HitcSpider(scrapy.Spider):
    name = 'hitc'
    allowed_domains = ['hitc.com']
    start_urls = url_selector.get_urls(allowed_domains)

    def parse(self, response):
        url = response.url
        datetime = response.css(".insidebar time::attr(datetime)").extract_first()
        headline = response.css("header h1 ::text").extract_first()
        subhead = " ".join(response.css(".post-summary ::text").extract())
        author = response.css(".post-author ::text").extract_first()
        body_text = " ".join(response.css(".post-content p ::text").extract())

        body_text = body_text.replace(subhead, "")

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice

#Twt: 
# http://www.hitc.com/en-gb/2018/07/07/do-weekend-wouldnt-pay-5p-west-ham-fans-react-to-haris-seferovic/