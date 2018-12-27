# -*- coding: utf-8 -*-
import scrapy
import re
from property.items import JiwuItem

class WlmqSpider(scrapy.Spider):
    name = 'wlmq'
    allowed_domains = ['wlmq.jiwu.com']
    start_urls = ['http://wlmq.jiwu.com/loupan']

    def parse(self, response):
        for url in response.xpath('//a[@class="index_scale"]/@href').extract():
            yield scrapy.Request(url, self.parse_html)

        nextpage = response.xpath('//a[@class="tg-rownum-next index-icon"]/@href').extract_first()
        if nextpage:
            yield scrapy.Request(nextpage, self.parse)

    def parse_html(self, response):
        '''
        解析每个房产信息的详情页面，生成item
        :param response:
        :return:
        '''
        pattern = re.compile('<script type="text/javascript">.*?lng = \'(.*?)\';.*?lat = \'(.*?)\';.*?bname = \'(.*?)\';.*?'
                             'address = \'(.*?)\';.*?price = \'(.*?)\';',re.S)
        item = JiwuItem()
        results = re.findall(pattern, response.text)
        for result in results:
            item['name'] = result[2]
            item['address'] = result[3]
            # 对价格判断只要数字，如果为空就设置为0
            pricestr = result[4]
            pattern2 = re.compile('(\d+)')
            s = re.findall(pattern2, pricestr)
            if len(s) == 0:
                item['price'] = 0
            else:
                item['price'] = s[0]
            item['lng'] = result[0]
            item['lat'] = result[1]
        yield item
