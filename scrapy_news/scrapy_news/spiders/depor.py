# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl depor

class DeporSpider(scrapy.Spider):
    name = 'depor'
    allowed_domains = ['depor.com']
    source = 'Depor'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):
        url = response.url
        datetime = response.css(".news-date ::attr(datetime)").extract_first()
        headline = response.css(".news-title ::text").extract_first()
        subhead = response.css(".news-summary ::text").extract_first()
        author = response.css(".author-name a ::text").extract_first()
        body_text = " ".join(response.css(".news-text-content p ::text").extract())

        media_text = " ".join(response.css(".news-text-content .news-media-description p ::text").extract())
        body_text = body_text.replace(media_text,"")

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice
