
'''
Author : Liu Yang
Date : Aug 20 
'''
import scrapy
import json
import time
#from BitcoinAddrSpider.items import BitcoinaddrspiderItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
class BitcoinAddrSpider(CrawlSpider):
	item={}
	name="bitcoinaddr"
	allowed_domains = ["bitcointalk.org"]
	start_urls = [
		"https://bitcointalk.org/index.php?board=1.0"
    ]

	rules=(
		Rule(LinkExtractor(allow=('board'))),
		Rule(LinkExtractor(allow=('topic')),callback='parse_item'),
	)
  
	def parse_item(self, response):
		#print response.xpath('//tbody').extract() , "!!!"
		for line in response.css(".signature"):
			#print line.extract(), ' !!! ';
			#_item = BitcoinaddrspiderItem()
			if(line.xpath('text()').re(r"(1[1-9A-HJ-NP-Za-km-z]{26,33})")==[]):
				continue
			Addr = line.xpath('text()').re(r"(1[1-9A-HJ-NP-Za-km-z]{26,33})")[0]
			print Addr ,"123!!!\n"
			Username=line.xpath('../../../tr[1]/td[1]/b/a/text()').extract()[0]
			if Username == "" or Addr=="":
				continue
			try:
				self.item[Username].append(Addr)
				self.item[Username]=list(set(self.item[Username]))
			except KeyError:
				self.item[Username]=[Addr]
			print Username ,' : ',  Addr, "!!!!\n"
			#yield item

	def closed(self,reason):
		print self.item,"!!!"
		fileHandle = open ( 'output.json', 'w' )
		fileHandle.write (json.dumps(self.item))
		fileHandle.close() 


