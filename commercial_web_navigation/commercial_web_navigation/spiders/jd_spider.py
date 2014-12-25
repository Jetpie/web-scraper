import scrapy

from commercial_web_navigation.items import JDItem

class JDSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["jd.com"]
    start_urls = [
        "http://www.jd.com/allSort.aspx"
    ]

    def parse(self, response):
        # 1st level category are <h2>s
        h2s = response.xpath('//h2')
        1st = response.xpath('//div[@class="m"]')
        for sel in dts:
            item = JDItem()
            item['category'] = sel.xpath('a/text()').extract()
            yield item
