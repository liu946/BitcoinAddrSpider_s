# -*- coding: utf-8 -*-

# Scrapy settings for BitcoinAddrSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'BitcoinAddrSpider'
DEPTH_LIMIT = 2
SPIDER_MODULES = ['BitcoinAddrSpider.spiders']
NEWSPIDER_MODULE = 'BitcoinAddrSpider.spiders'
DOWNLOAD_DELAY = 0.4 

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'BitcoinAddrSpider (+http://www.yourdomain.com)'
