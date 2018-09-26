# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl fcbn

class DNSpider(scrapy.Spider):
    name = 'fcbn'
    allowed_domains = ['fcbn.pt']
    source = 'FC Barcelona Noticias'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):
        url = response.url
        datetime = response.css(".noti_publish ::text").extract_first()
        headline = response.css(".noti_title ::text").extract_first()
        subhead = " ".join(response.css(".noti_subtitle ::text").extract())
        author = response.css(".noti_author ::text").extract_first()
        body_text = " ".join(response.css(".noti_body ::text").extract())

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice