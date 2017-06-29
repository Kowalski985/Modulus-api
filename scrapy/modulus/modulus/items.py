# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PreApprovedMapping(scrapy.Item):
	NUSCode = scrapy.Field()
    PUCode = scrapy.Field()
    PUName = scrapy.Field()

class Module(scrapy.Item):
	ModuleCode = scrapy.Field()
	ModuleTitle = scrapy.Field()
	ModuleDescription = scrapy.Field()
	Link = scrapy.Field()

class NusModule(Module):
	ModuleCredit = scrapy.Field()
	ModuleWorkLoad = scrapy.Field()
