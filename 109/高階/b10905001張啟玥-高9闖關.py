import requests,bs4
from bs4 import BeautifulSoup


url='https://www.ptt.cc/bbs/Food/index.html'

headers={
'referer':'https://www.ptt.cc/',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

r = requests.get(url , headers = headers)   
ptthtml = requests.get(url, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')

articles = 0                # 本頁面文章數量
pttdivs = objSoup.find_all('div', 'r-ent')
for p in pttdivs:
    if p.find('a'):
        articles += 1          
    
articles = []                                           # 本頁面文章
pttdivs = objSoup.find_all('div', 'r-ent')
for p in pttdivs:
    if p.find('a'):
        title = p.find('a').text
        author = p.find('div', 'author').text
        href = p.find('a')['href']
        push_num = p.find('div', 'nrec').text
        ptime = p.find('div', 'date').text
        articles.append({'title':title,                 # 文章標題
                         'author':author,               # 文章作者
                         'href':href,                   # 文章超連結
                         'ptime':ptime,                 # 貼文時間
                         'push_num':push_num,           # 推文數
                        })
        
url_ppt = 'https://www.ptt.cc'
Food = '/bbs/Food/index.html'

ptthtml = requests.get(url_ppt+Food, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')

pttdivs = objSoup.find_all('div', 'r-ent')
href = pttdivs[0].find('a')['href']                                 # 文章超連結

Food_html = requests.get(url_ppt+href, cookies={'over18':'1'})    # 進入超連結
Food_soup = bs4.BeautifulSoup(Food_html.text, 'lxml')   

Food_divs = Food_soup.find('div', id='main-content')
items = Food_divs.find_all('div', 'article-metaline')

for item in items:                                                  # 列印標題
    field = item.find('span', 'article-meta-tag')
    print(field.text,end=' : ')
    field_data = item.find('span', 'article-meta-value')
    print(field_data.text)       
mylist = list(Food_divs) 
        
count = 0                                               # 文章編號計數器
for article in articles:
    count += 1
    print('文章編號 : ', count)
    print('貼文時間 : ', article['ptime'])
    print('文章作者 : ', article['author'])
    print('文章標題 : ', article['title'])    
    print('文章連結 : ', article['href']) 
    print('內文 : ')
    print(mylist[4].strip()) 
    print()
                                         
    
    
    
    
    
    
    
    
    