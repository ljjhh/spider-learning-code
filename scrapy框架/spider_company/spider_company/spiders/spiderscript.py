import scrapy
from ..items import SpiderCompanyItem
class SpiderscriptSpider(scrapy.Spider):
    name = 'spiderscript'
    #allowed_domains = ['www.XXX.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        div_list=response.xpath('//*[@id="content"]/div/div[2]/div')
        #print(response.text)
        #print(div_list)
        print("hello")
        all_data=[]
        for div in div_list:
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            content = div.xpath('./a[1]/div/span//text()').extract()
            #列表调用了extract对象则表示将select对象列表元素中的data提取出来
            print(author)
            print(content)
            content=''.join(content)

            item = SpiderCompanyItem()
            item['author']=author
            item['content']=content

            yield item
