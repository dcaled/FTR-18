# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl footballespana

class FootballEspanaSpider(scrapy.Spider):
    name = 'footballespana'
    allowed_domains = ['football-espana.net']
    source = 'Football Espana'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):
        url = response.url
        datetime = response.css(".date ::text").extract_first()
        headline = response.css(".title ::text").extract_first()
        subhead = ""
        author = response.css(".submitted ::text").extract_first()
        body_text = " ".join(response.css(".content p ::text").extract())

        body_text = body_text.replace("See the latest La Liga predictions and betting tips with  Eurotips.co.uk", "")

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice

