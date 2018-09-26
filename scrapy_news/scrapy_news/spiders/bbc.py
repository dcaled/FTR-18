# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl bbc

class BBCSpider(scrapy.Spider):
    name = 'bbc'
    allowed_domains = ['bbc.com']
    source = 'BBC'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):
        url = response.url
        datetime = response.css(".abbr-on ::text").extract_first()
        headline = response.css(".story-headline ::text").extract_first()
        subhead = response.css(".sp-story-body__introduction ::text").extract_first()
        author = ""
        body_text = " ".join(response.css(".story-body p ::text").extract())

        body_text = body_text.replace("Media playback is not supported on this device", "")
        body_text = body_text.replace(" Find all the latest football transfers  on our dedicated page.", "")
        body_text = body_text.replace(subhead, "")


        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice

