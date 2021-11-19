import requests
from bs4 import BeautifulSoup
import time
import re

url="https://www.umei.cc/weimeitupian/"

headrs={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53"
}

resp1=requests.get(url,headers=headrs)
resp1.encoding='utf-8'

page1=BeautifulSoup(resp1.text,"html.parser")

div_all=page1.find("div",class_='TypeList')
a_individual=div_all.find_all("a")
for a in a_individual:
    url1=a.get('href')
    name=a.find('span')
    name_str=re.sub('[^\u4e00-\u9fa5|a-z|A-z]+', '',name.text)#因为图片命名的问题只保留汉字和英文字母
    resp2=requests.get('https://www.umei.cc'+url1,headers=headrs)
    time.sleep(0.5)
    resp2.encoding='utf-8'
    page2=BeautifulSoup(resp2.text,"html.parser")
    url3 = page2.find('div',class_='ImageBody').find("img").get('src')
    resp3=requests.get(url3)
    print("图片：{0}".format(name_str)+"请求成功！！ 正在下载中！！")
    with open('picture/'+name_str+'.jpg','wb') as f:
        f.write(resp3.content)
    print("图片：{0}".format(name_str)+"正在下载完成！！")
    time.sleep(0.5)
print("完成！！！！！！......")
resp2.close()
resp3.close()
resp1.close()
