# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import TutorialItem
class DmonSpiderSpider(scrapy.Spider):
    name = 'dmon_spider'
    allowed_domains = ['dmoz.org']
    start_urls = ['https://www.amazon.cn/s?ie=UTF8&search-type=ss&index=books&field-keywords=Python%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E4%B8%8E%E6%8C%96%E6%8E%98%E5%AE%9E%E6%88%98&tag=baiduiclickcn-23&ref=Book_17417_zhj_5279']

    def parse(self, response):
        # filename = response.url.rsplit('/')[2] + '.html'
        # with open(filename,'wb') as e:
        #     e.write(response.body)
        lis =response.xpath('//*[@id="result_1"]/div/div/div/div[2]/div[1]/div[1]/a/h2')
        for li in lis:
            item = TutorialItem()
            item['title'] = li.xpath('a/text()').extract()
            item['link'] = li.xpath('a/@href')
            item['desc'] = li.xpath('text()')
            yield item