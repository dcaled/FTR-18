# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl fichajes.com

class FichajesComSpider(scrapy.Spider):
    name = 'fichajes.com'
    allowed_domains = ['fichajes.com']
    source = 'Fichajes.com'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):

        url = response.url
        datetime = response.css("time ::attr(datetime)").extract_first()
        headline = response.css(".article h1 ::text").extract_first()
        subhead = response.css(".article h2 ::text").extract_first()
        author = response.css(".name ::text").extract_first()
        body_text = " ".join(response.css(".article-text ::text").extract())
        
        twt_text = " ".join(response.css(".twitter-tweet p ::text").extract())
        body_text = body_text.replace(twt_text, "")
              
        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)

        yield notice

#Twt
#http://www.fichajes.com/breves/chelsea-las-primeras-palabras-de-mateo-kovacic_138960
#http://www.fichajes.com/breves/el-atletico-de-madrid-dice-adios-a-andre-moreira_138630