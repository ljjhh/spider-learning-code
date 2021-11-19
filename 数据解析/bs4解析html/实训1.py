from bs4 import BeautifulSoup
import requests

url="https://price.21food.cn/market/674.html"
headrs={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53"
}
resp=requests.get(url,headers=headrs)

#print(resp.text)

page=BeautifulSoup(resp.text,"html.parser") #定义一个BeautifulSoup对象
table1=page.find(name="div",class_="sjs_top_cent_erv")
table2=page.find_all("div",attrs={"class":"sjs_top_cent_erv"})#两种方法都行
print(type(table1))
print(type(table2))
'''for i in table2:
    print(i)'''
item1=table1.find("ul") #find之后可以继续find因为他返回的是一个对象<class 'bs4.element.Tag'>
#print(item1)
item2=item1.find_all("tr")#而find_all要想继续必须将得到的<class 'bs4.element.ResultSet'>对象分开
#print(item2)

dic_date={}
lst_data=[]
for i in item2:
    tds=i.find_all("td")
    print(tds)
    print()
    dic_date= {
    'name': tds[0].text,
    'market': tds[1].text,
    'highest': tds[2].text,
    'lowest': tds[3].text,
    'average': tds[4].text,
    'date': tds[5].text
    }
    lst_data.append(dic_date)
    print(lst_data)

print(lst_data)


resp.close()
