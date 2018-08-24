# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl dailystar

class DailyStarSpider(scrapy.Spider):
    name = 'dailystar'
    allowed_domains = ['dailystar.co.uk']
    start_urls = url_selector.get_urls(allowed_domains)

    def parse(self, response):

        url   = response.url
        datetime = response.css("time ::attr(datetime)").extract_first()
        headline = response.css("h1 ::text").extract_first()
        subhead = response.css(".lead ::text").extract_first()
        author = response.css(".author ::text").extract_first()
        body_text = " ".join(response.css(".text-description p ::text").extract())

        bqt_text = " ".join(response.css(".text-description blockquote p ::text").extract())
        str_text = " ".join(response.css(".text-description p strong ::text").extract())
        body_text = body_text.replace(bqt_text, "")
        body_text = body_text.replace(str_text, "")

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)

        yield notice


