# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# 設定網址
url='https://tw.news.yahoo.com'

# 擷取此網頁的原始資料，得到一個回應物件res
res=requests.get(url)

# 輸出回應物件的訊息，若是200代表有資料，若不是200代表沒有擷取到資料
print(res)

# 輸出回應物件的內容
print(res.text)

# 將網頁資料進行解析
bs=BeautifulSoup(res.text,'lxml')

# 取出標籤(tag)名稱為li，屬性(attrib)內容為Pos(r)的資料
data1=bs.find_all('li','Pos(r)')

# 設定編號
x=1
print(data1)

# 使用迴圈方式，將資料逐筆取出並輸出
for i in data1:
    con=i.find('a').text
    print(x,con,sep='.')
    x=x+1