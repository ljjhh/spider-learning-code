import requests
import re
import csv
url="https://movie.douban.com/top250"

headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53"
}

response=requests.get(url,headers=headers)
obj=re.compile(r'<div class="item">.*?<img width="100" alt=(?P<name>.*?) src.*?导演: (?P<daoyan>.*?)&nbsp.*?'
               r'<span class="rating_num" property="v:average">(?P<pinfen>.*?)</span>.*?<span>(?P<pingjia>.*?)</span>',re.S)

result=obj.finditer(response.text)
f=open("data.csv",'w',encoding='utf-8')
csvwiter=csv.writer(f)
for i in result:
    #print(i.group("name"))
    #print(i.group('daoyan'))
    #print(i.group('pinfen'))
    #print(i.group('pingjia'))
    dic=i.groupdict()
    csvwiter.writerow(dic.values())
f.close()

