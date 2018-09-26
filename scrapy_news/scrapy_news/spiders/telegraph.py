# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl telegraph

class TelegraphSpider(scrapy.Spider):
    name = 'telegraph'
    allowed_domains = ['telegraph.co.uk']
    source = 'The Telegraph'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):
        url = response.url
        datetime = response.css(".component-content time::attr(datetime)").extract_first()
        headline = response.css("h1.headline__heading ::text").extract_first()
        subhead = response.css(".lead-asset-caption ::text").extract_first()
        author = response.css(".byline__author-name a ::text").extract_first()
        bt_lst = response.css(".articleBodyText p ::text").extract()


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
