import scrapy


class MazumabotSpider(scrapy.Spider):
    name = 'mazumabot'
    allowed_domains = ['buy.mazumamobile.com.au']
    start_urls = ['http://buy.mazumamobile.com.au/']

    def parse(self, response):
        links = response.css("site-nav__label::text").extract()
        
        for link in links:
            scraped_info = {
                'URL': link
                }
        yield scraped_info 
