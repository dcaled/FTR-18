# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl mundodeportivo

class MundoDeportivoSpider(scrapy.Spider):
    name = 'mundodeportivo'
    allowed_domains = ['mundodeportivo.com']
    start_urls = url_selector.get_urls(allowed_domains)

    def parse(self, response):

        url = response.url
        datetime = response.css(".story-leaf-datetime ::attr(datetime)").extract_first()
        headline = response.css(".story-leaf-title ::text").extract_first()
        subhead = response.css(".story-leaf-subtitle ::text").extract_first()
        author = response.css(".story-leaf-author-link ::text").extract_first()
        body_text = " ".join(response.css(".story-leaf-txt-p p ::text").extract())

        rel_text = " ".join(response.css('p.story-leaf-relatednews-epigraph ::text').extract())
        body_text = body_text.replace(rel_text, "")

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)

        yield notice

#Twt
#https://www.mundodeportivo.com/futbol/atletico-madrid/20180710/45818042789/el-atletico-hace-oficial-el-fichaje-de-adan.html
