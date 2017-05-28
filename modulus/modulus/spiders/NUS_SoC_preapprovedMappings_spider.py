import scrapy

#to run crawler: scrapy crawl NUS_SoC_preApproved -o NUS_SoC_preApproved.json
class NUSSoCPreSpider(scrapy.Spider):
    name = "NUS_SoC_preApproved"
    start_urls = [
        'https://comp.nus.edu.sg/programmes/ug/beyond/sep/sepnoc/'
    ]

    def parse(self, response):
        mainBody = response.xpath('//div[@itemprop = "articleBody"]')
        uniCount = 0
        for partnerUni in mainBody.xpath('.//h2'):
            uniCount += 1
            uniName = partnerUni.css('h2::text').extract() 
            for module in mainBody.xpath('.//ul[$val]/table/tbody/tr', val = uniCount):
                #NUS module is in [0], PU module is [1] 
                modCodes = module.css('b::text').extract()
                #temp not using it for now
                modTitles = module.css('td::text').extract()
                if (len(modCodes) != 0):
                    yield {
                        'NUSCode' : modCodes[0],
                        'PUCode' : modCodes[1],
                        'PUName' : uniName[0]
                    }