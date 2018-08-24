# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl goal

class GoalSpider(scrapy.Spider):
    name = 'goal'
    allowed_domains = ['goal.com']
    start_urls = url_selector.get_urls(allowed_domains)

    def parse(self, response):

        url = response.url
        datetime = response.css("time ::attr(datetime)").extract_first()
        headline = response.css(".article-headline ::text").extract_first()
        subhead = response.css(".teaser ::text").extract_first()
        author = response.css(".name ::text").extract_first()
        body_text = " ".join(response.css(".body p ::text").extract())

        rel_text = " ".join(response.css(".widget-inline-related-articles ::text ").extract())
        body_text = body_text.replace(rel_text, "") 

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)

        yield notice

#Twt
#http://www.goal.com/br/not%C3%ADcias/mateo-kovacic-ja-posa-com-a-camisa-do-chelsea-apos-ser/betcue5ge4391gyhxz5hxmkq0

#
#http://www.goal.com/br/not%C3%ADcias/arsenal-prepara-oferta-irrecusavel-a-lucas-vazquez-do-real/ntw6y5r9ygyr1qhvkyk4pw7dp