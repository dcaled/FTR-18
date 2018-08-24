# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl teamtalk

class TeamtalkSpider(scrapy.Spider):
    name = 'teamtalk'
    allowed_domains = ['teamtalk.com']
    start_urls = url_selector.get_urls(allowed_domains)

    def parse(self, response):
        url = response.url
        datetime = response.css(".article__header p ::text").extract_first()
        headline = response.css(".article__header h1 ::text").extract_first()
        subhead = response.css(".article__body strong ::text").extract_first()
        author = ""
        body_text = " ".join(response.css(".article__body p ::text").extract())

        i_text = " ".join(response.css(".article__body p i ::text").extract())
        script_text = " ".join(response.css(".article__body p script ::text").extract())
        
        body_text = body_text.replace(subhead, "")
        body_text = body_text.replace(script_text, "")
        body_text = body_text.replace(i_text, "")

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice

#Fix:
#More from Planet Sport
#https://www.teamtalk.com/news/bruce-admits-it-will-be-difficult-to-keep-grealish-away-from-tottenham