# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl maisfutebol

class MaisfutebolSpider(scrapy.Spider):
    name = 'maisfutebol'
    allowed_domains = ['maisfutebol.iol.pt']
    source = 'Maisfutebol'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):
        url = response.url
        datetime = response.css(".date ::text").extract_first()
        headline = response.css("h1 ::text").extract_first()
        subhead = response.css("h2 ::text").extract_first()
        author = response.css(".autores a ::text").extract_first()
        body_text = " ".join(response.css(".articleBody p ::text").extract())

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice
#Twt
#http://www.maisfutebol.iol.pt/espanha/celta-vigo/oficial-sevilha-contrata-sergi-gomez

