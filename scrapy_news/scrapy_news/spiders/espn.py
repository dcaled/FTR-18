# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl espn

class ESPNSpider(scrapy.Spider):
    name = 'espn'
    allowed_domains = ['espn.com','espn.com.br','espn.co.uk']
    start_urls = url_selector.get_urls(allowed_domains)

    def parse(self, response):
        url = response.url
        datetime = response.css(".timestamp ::attr(data-date)").extract_first()
        headline = response.css(".article-header h1 ::text").extract_first()
        subhead = ""
        author = response.css(".author ::text").extract_first()
        body_text = " ".join(response.css(".article-body p ::text").extract())

        related_text = " ".join(response.css(".article-body .editorial p ::text").extract())
        prom_text = " ".join(response.css(".article-body .inline-track p ::text").extract())
        #related_text = " ".join(response.css(".article-body strong ::text").extract())
        body_text = body_text.replace(related_text, "")
        body_text = body_text.replace(prom_text, "")

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice

#Twt
#http://kwese.espn.com/football/soccer-transfers/story/3580918/everton-confirm-signing-of-defender-lucas-digne-from-barcelona
#Related
#http://www.espn.com/soccer/soccer-transfers/story/3590067/tottenham-told-aston-villas-jack-grealish-not-for-sale-at-any-price-sources
#Live Blog
#http://www.espn.com/soccer/blog/transfer-talk/79/post/3560433/transfer-talk-real-madrid-add-eden-hazard-to-list-of-cristiano-ronaldo-replacements
#http://www.espn.com/soccer/blog/transfer-talk/79/post/3511582/transfer-talk-man-united-keen-on-gareth-bale-but-price-is-now-200m
#http://www.espn.com/soccer/blog/transfer-talk/79/post/3563330/transfer-talk-manchester-united-and-real-madrid-in-gareth-bale-talks
