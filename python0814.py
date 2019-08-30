# -*- coding: utf-8 -*-
"""Python0814.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZLAo5odpyf5aMvAAkkno6FMJ5iUFjpzx

## **101**
"""

import json

with open('read.json','r',encoding='UTF-8') as fp:
    Li = json.load(fp)
with open('write.csv','w',encoding='UTF-8') as fp:
    for i in Li:
        title = i['title']
        sUnit = i['showUnit']
        sDate = i['startDate']
        eDate = i['endDate']
        fp.write('{},{},{},{}\n'.format(title,sUnit,sDate,eDate))

"""## **102**"""

import xml.etree.ElementTree as ET

tree = ET.parse('read.xml')
root = tree.getroot()

with open('write.csv','w',encoding='UTF-8') as fp:
    for i in root:
        sno = i.find('sno').text
        sna = i.find('sna').text
        tot = i.find('tot').text
        fp.write('{},{},{}\n'.format(sno,sna,tot))

"""## **103**"""

import json

with open('read.json','r',encoding='UTF-8') as fp:
    Li = json.load(fp)
    
with open('write.yaml','w',encoding='UTF-8') as fp:
    for i in Li:
        fp.write('- 投保薪資等級: {}\n'.format(i['投保薪資等級']))
        fp.write('  月投保薪資: {}\n'.format(i['月投保薪資']))
        fp.write('  月薪資總額: {}\n'.format(i['月薪資總額']))
        fp.write('  身分別: {}\n'.format(i['身分別']))

"""## **104**"""

import json

dict1 = {
      'people': 
        [{
        'id': '1',
        'name': 'Peter',
        'country': 'Taiwan'
        },
        {
        'id': '2',
        'name': 'Jack',
        'country': 'USA'
        },
        {
        'id': '3',
        'name': 'Cindy',
        'country': 'Japan'
        }]
     }

with open('write.json', 'w', encoding='utf-8') as fp:
    fp.write( json.dumps( dict1 ) )

"""## **安裝requests**"""

!pip install requests2

"""## **requests.get(url)**"""

import requests

yahooRes = requests.get('https://tw.yahoo.com/')

print(yahooRes.headers)  #瀏覽網頁標頭
print()
print(yahooRes.text)  #瀏覽網頁原始檔文字

"""## **requests.get(url,params = None)**"""

import requests

url = 'https://tw.search.yahoo.com/search'
param = { 'fr':'yfp-search-sb' , 'p':'java' }

yahooRes = requests.get( url , params = param)

print(yahooRes.text)

"""## **requests.get(url, cookies={})**"""

import requests

pttRes = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html', cookies={'over18': '1’})

print(pttRes.text)

"""## **requests內建的json()函數**"""

import requests

url = 'http://opendata.epa.gov.tw/webapi/Data/ATM00766/?$orderby=SiteId%20desc&$skip=0&$top=1000&format=json' 

aqiRes = requests.get ( url )

aqiLi = aqiRes.json()

for i in aqiLi : print(i)

"""## **requsts.post(url,data={})**"""

import requests

url = 'https://m.thsrc.com.tw/tw/TimeTable/SearchResultList'
datas = {'startStation': '977abb69-413a-4ccf-a109-0272c24fd490',
'endStation': '3301e395-46b8-47aa-aa37-139e15708779',
'theDay': '2019/08/14',
'timeSelect': '14:00',
'waySelect': 'DepartureInMandarin'}

srcRe=requests.post(url, data=datas)
print(srcRe.text)

"""## **安裝BeautifulSoup**"""

!pip install beautifulsoup4

"""## **爬取在奇摩搜尋python的結果網頁**"""

from bs4 import BeautifulSoup as BS
import requests

url = 'https://tw.search.yahoo.com/search'
param = { 'fr':'yfp-search-sb' , 'p':'python' }

yahooRes = requests.get( url , params = param )

soup = BS(yahooRes.text,'lxml')
# print(soup.prettify()) #觀察網頁原始碼
# print(soup)

"""## **element.find('tag')**"""

yahoo = soup.find('title')
print (yahoo.string)

"""## **element.findAll('tag',class_='class')**"""

result = soup.findAll('a',class_=' ac-algo fz-l lh-20 tc d-ib va-mid')
for i in result: print(i.string)

"""## **element.select('path')**"""

result = soup.select('#web .va-mid')
for i in result:
  print(i.string)

"""## **爬取ptt八卦版網頁(使用cookies)**"""

from bs4 import BeautifulSoup as BS
import requests

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
pttRes = requests.get(url , cookies={'over18': '1'})
soup = BS(pttRes.text,'lxml')
print(pttRes.text)
# print(soup.prettify()) #觀察網頁原始碼
# print(soup)

"""## **爬取標題**"""

result = soup.select('.title a')

# for i in result:
#     print(i.string)
    
for i in range(0,(len(result)-5)): 
    print(result[i].string)

"""## **爬取tag屬性**"""

result = soup.select('.title a')

for i in result:
    print('https://www.ptt.cc'+i.get('href'))

"""## **爬取PTT八卦版練習**"""

from bs4 import BeautifulSoup as BS
import requests

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
pttRes = requests.get(url , cookies={'over18': '1'})
soup = BS(pttRes.text,'html.parser')

pushResu = soup.select('.nrec')
titleResu = soup.select('.title a')

for i in range(0,(len(result)-5)): 
    if pushResu[i].string == None:
        print('推文數:',0)
    else:
        print('推文數:',pushResu[i].string)
    print('標題:',titleResu[i].string)
    print('網址:','https://www.ptt.cc'+titleResu[i].get('href'))
    print()

"""## **201**"""

import requests

url = 'http://tqc.codejudger.com:3000/target/5201.html'
doc = requests.get(url).text

str1 = input('請輸入欲搜尋的字串 : ')
strCount = doc.count(str1)

if strCount == 0:
    print(str1, '搜尋失敗')
else:
    print(str1, '搜尋成功')
    print(str1, '出現', strCount,'次')

"""## **202**"""

from bs4 import BeautifulSoup as BS

with open('read.html','r',encoding='UTF-8') as fp:
    li = BS(fp.read(),'html.parser')
    
titleLi = li.findAll('th')
dataLi = li.findAll('td')

dataLi1 = []

for i in dataLi:
    if i.string != None:
        dataLi1.append(i.string)
        
with open('write.csv','w',encoding='UTF-8') as fp:
    fp.write('{},{}\n'.format(titleLi[0].string,titleLi[1].string))
    for i in range(0,len(dataLi1),2):
        fp.write('{},{}\n'.format(dataLi1[i],dataLi1[i+1]))