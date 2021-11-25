# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class SpiderCompanyPipeline(object):
    fp= None
    #重写父类的方法 该方法只会在开始爬虫的时候调用一次
    def open_spider(self,spider):
        print("开始爬虫")
        self.fp = open('./qiubai.txt','w',encoding="utf-8")
    def process_item(self, item, spider):  #该方法可以接收到提交过来的item对象
        author = item['author']
        content = item['content']
        self.fp.write(author+":"+content+'\n')

        return item  #会传递给下一个管道类
    def close_spider(self,spider):  #重写父类方法，只在爬虫结束的时候调用一次
        print("结束爬虫")
        self.fp.close()
class mysqlPileLine(object):
    conn=None
    cursor=None
    def open_spider(self,spider):
        self.conn=pymysql.connect(host='localhost',port=3306,user="root",password='5674389210qazplm',db='qiubai')
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS xiushi")
        self.cursor.execute(
            "CREATE TABLE `xiushi`(`id` bigint(20) NOT NULL AUTO_INCREMENT,"
            "`author` varchar(255) ,`content` text,PRIMARY KEY (`id`))")
    def process_item(self,item,Spider):
        self.cursor = self.conn.cursor()
        insert='insert into xiushi (author,content) value (%s,%s)'
        try:
            value=(item['author'], item['content'])
            self.cursor.execute(insert,value)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
            return item #返回给下一个管道类

    def close_spider(self,spider):
        self.conn.close()
        self.cursor.close()
