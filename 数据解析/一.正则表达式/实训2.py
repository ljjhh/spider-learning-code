import requests
import re

url1="https://www.dygod.net/"

obj1 = re.compile(r"迅雷电影资源.*?<ul>.*?<li>(?P<content>.*?)</ul>",re.S)
obj2 = re.compile(r'<li><a href=\'(?P<ul>.*?)\'.*?title="(?P<name>.*?)"',re.S)
obj3 = re.compile(r"<li><a href=\"jianpian://pathtype=url&path=()(?P<downloadsite>.*?)[\u4e00-\u9fa5]")

resp1=requests.get(url1,verify=False)
resp1.encoding="gb2312"
result1=obj1.search(resp1.text)
str1=result1.group()
result2=obj2.finditer(str1)
with open('film.txt','w',encoding='gbk') as f:
    for it in result2:
        url2=url1+it.group('ul').strip(r'/')
        print(it.group('ul'))
        resp2=requests.get(url2,verify=False)
        resp2.encoding="gb2312"
        result3=obj3.search(resp2.text)
        f.write(it.group('name'))
        f.write("的下载地址为")
        f.write(result3.group('downloadsite')+"\n")

resp1.close()
resp2.close()
