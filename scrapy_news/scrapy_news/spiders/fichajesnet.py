# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl fichajes.com

class FichajesNetSpider(scrapy.Spider):
    name = 'fichajes.net'
    allowed_domains = ['fichajes.net']
    start_urls = url_selector.get_urls(allowed_domains)

    def parse(self, response):

        url = response.url
        datetime = response.css(".md-info-date ::attr(datetime)").extract_first()
        headline = response.css("h1 ::text").extract_first()
        subhead = response.css("#node-story-full-group-header h2 ::text").extract_first()
        author = " ".join(response.css(".author ::text").extract())
        body_text = " ".join(response.css(".content-body p ::text").extract())

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)

        yield notice