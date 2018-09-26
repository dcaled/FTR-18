# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl ojogo

class OJogoSpider(scrapy.Spider):
    name = 'ojogo'
    allowed_domains = ['ojogo.pt']
    source = 'O Jogo'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):

        url = response.url
        datetime = response.css(".t-a-info-1 time ::attr(datetime)").extract_first()
        headline = response.css(".t-i h1 ::text").extract_first()
        subhead = response.css(".t-a-c-intro-1 ::text").extract_first()
        author = response.css(".t-a-info-author ::text").extract_first()
        bt_lst = response.css(".t-a-c-wrap p ::text").extract()
 
        for i in range(len(bt_lst)):
            bt_lst[i] = bt_lst[i].strip()
        body_text = " ".join(bt_lst)

        body_text = body_text.replace(subhead, "")


        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)

        yield notice



