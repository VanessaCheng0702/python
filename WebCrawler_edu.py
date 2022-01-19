# -*- coding: utf-8 -*-
import requests,os,urllib
from bs4 import BeautifulSoup

url='https://www.edu.tw/'
html=requests.get(url)
html.encoding="utf-8"
bs=BeautifulSoup(html.text,'html.parser')
pics_dir="pics"

if not os.path.exists(pics_dir):
    # 在工作目錄下建立目錄pics來儲存圖片
    os.mkdir(pics_dir)
# 用串列取得所有<img>標籤的內容
all_links=bs.find_all('img')
for link in all_links:
    # 讀取src屬性值的內容
    src=link.get('src') 
    # 將src字串轉成串列attrs
    attrs=[src]
    for attr in attrs:
        # 讀取.jpg或.png檔
        if attr!=None and ('.jpg' in attr or '.png' in attr):
            # 設定圖檔完整路徑
            full_path=attr
            # 從網址的最右側取得圖檔的名稱
            file_n=full_path.split('/')[-1]
            print('===============')
            print('圖檔完整路徑:',full_path)            
            try:  
                # 儲存圖片程式區塊
                image=urllib.request.urlopen(full_path)
                #(wb用byte寫入)
                f=open(os.path.join(pics_dir,file_n),'wb') 
                f.write(image.read())
                print('下載成功:%s' %(file_n))
                f.close()
            except: #無法儲存圖片程式區塊
                print('無法下載:%s' %(file_n))
