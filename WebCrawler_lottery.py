# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url='https://www.taiwanlottery.com.tw/index_new.aspx'
html=requests.get(url)
bs=BeautifulSoup(html.text,'html.parser')

# 取出class 名稱為contents_box02的串列
# data1=bs.select(".contents_box02")
data1=bs.find()
# 在第3個區塊中抓出黃球
data2=data1[2].find_all('div',{'class':'ball_tx'})
print('大樂透黃球資料:')
print(data2)
print('===========================')

title=data1[2].find('span',{'class':'font_black15'}).text
print(title)
# 大樂透號碼

print('開出順序:',end='')
for n in range(0,6):
    print(data2[n].text,end=' ')
print("\n大小順序:",end="")
for n in range(6,len(data2)):
    print(data2[n].text,end=' ')
    
# 特別號
red=data1[2].find('div',{'class':'ball_red'})
print("\n特別號(紅球):%s" %(red.text))
