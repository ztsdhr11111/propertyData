# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import workbook

class JiwuPipeline(object):
    wb = workbook.Workbook()
    ws = wb.active
    ws.append(['小区名称', '地址', '价格', '经度', '纬度'])

    def process_item(self, item, spider):
        jiwu = dict(item)
        line = [jiwu['name'], jiwu['address'], str(jiwu['price']), jiwu['lng'], jiwu['lat']]
        JiwuPipeline.ws.append(line)
        JiwuPipeline.wb.save('jiwu.xlsx')
        return item


