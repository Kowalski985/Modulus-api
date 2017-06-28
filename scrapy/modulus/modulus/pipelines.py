# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ModulusPipeline(object):

  def close_spider(self,spider):
    self.file.close()

  def writeToJson(self,item):
    output = json.dumps(dict(item)) + '\n'
    self.file.write(output)

class NusSocPreApprovedPipeline(ModulusPipeline):

  def open_spider(self,spider):
    self.file = open('NusSocPreApproved.json','w')

  def process_item(self,item,spider):
    writeToJson(item)
    return item

class NusModulesPipeline(ModulusPipeline):

  def open_spider(self,spider):
    self.file = open('NusModules.json','w')

  def process_item(self,item,spider):
    writeToJson(item)
    return item

class NtuModulesPipeline(ModulusPipeline):

  def open_spider(self,spider):
    self.file = open('NtuModules.json','w')

  def process_item(self,item,spider):
    writeToJson(item)
    return item