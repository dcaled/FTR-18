# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl metro

class MetroSpider(scrapy.Spider):
    name = 'metro'
    allowed_domains = ['metro.co.uk']
    start_urls = url_selector.get_urls(allowed_domains)

    def parse(self, response):

        url = response.url
        datetime = response.css(".post-date ::text").extract_first()
        headline = response.css(".post-title ::text").extract_first()
        subhead = ""
        author = response.css(".author ::text").extract_first().strip()
        body_text = " ".join(response.css('.article-body p ::text').extract())

        rel_lst = response.css('.zopo-title span ::text').extract()
        vid_text = " ".join(response.css("p.vjs-no-js ::text").extract())
        mor_text = " ".join(response.css(".mor-link ::text").extract())
        #twt_lst = response.css('.embed-twitter p ::text').extract()
        #igm_lst = response.css(".instagram-media p ::text").extract()

        for i in range(0,len(rel_lst),3):
            i_text = " ".join(rel_lst[i:i+3])
            body_text = body_text.replace(i_text, "")    
        
        body_text = body_text.replace(vid_text, "")
        body_text = body_text.replace(mor_text, "")
        
        #for i in twt_lst:
        #    body_text = body_text.replace(i.strip(), "")

        #for i in igm_lst:
        #    body_text = body_text.replace(i.strip(), "")

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)

        yield notice

#Twt
#https://metro.co.uk/2018/07/04/manchester-united-boss-jose-mourinho-tells-friends-keen-xherdan-shaqiri-7684184/

#Instagram

#Mais de um video
#https://metro.co.uk/2018/08/01/manchester-united-transfer-chief-flies-spain-seal-35million-yerry-mina-deal-7787869/

