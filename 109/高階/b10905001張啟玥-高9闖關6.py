import requests,bs4
from bs4 import BeautifulSoup
import pandas as pd
import json

url='https://www.ptt.cc/bbs/Food/index.html'

f = open('高9.csv','w',encoding='utf-8-sig',newline='')

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

  main_container = soup.find(id='main-container') #內文
  text = main_container.text
  text = text.split('\n')
  text = text[:]
  text = '\n'.join(text)
  f = open('高9.csv','at',encoding='utf-8-sig',newline='')
  f.write(text)
  f.close()