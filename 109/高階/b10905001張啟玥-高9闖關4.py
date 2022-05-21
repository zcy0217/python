import requests,bs4
from bs4 import BeautifulSoup
import pandas as pd
import json

url='https://www.ptt.cc/bbs/Food/index.html'

headers={
'referer':'https://www.ptt.cc/',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

r = requests.get(url , headers = headers)   
ptthtml = requests.get(url, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')

articles = 0                
pttdivs = objSoup.find_all('div', 'r-ent')
for p in pttdivs:
    if p.find('a'):
        articles += 1     

url_ppt = 'https://www.ptt.cc'
Food = '/bbs/Food/index.html'

ptthtml = requests.get(url_ppt+Food, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')

for i in range(articles): #幾篇文章執行幾輪
    
    pttdivs = objSoup.find_all('div', 'r-ent') #搜索文章超連結
    href = pttdivs[i].find('a')['href'] 
    
    Food_html = requests.get(url_ppt+href, cookies={'over18':'1'}) #進入文章超連結
    Food_soup = bs4.BeautifulSoup(Food_html.text, 'lxml')   
    
    soup = bs4.BeautifulSoup(Food_html.text,"html.parser")

    header = soup.find_all('span','article-meta-value') #上方4個欄位
    author = header[0].text #作者
    board = header[1].text #看版
    title = header[2].text #標題
    date = header[3].text #日期

    main_container = soup.find(id='main-container') #內文
    all_text = main_container.text
    pre_text = all_text.split('--')[0]
    texts = pre_text.split('\n')
    contents = texts[2:]
    content = '\n'.join(contents)  

    print('作者'+author)
    print('看板'+board)
    print('標題'+title)
    print('日期'+date)
    print(content)