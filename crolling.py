import time
import requests
from bs4 import BeautifulSoup

base_url = "https://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=06&fetchSize=40&PageNumber={}"


for n in range(1, 26):
    url = base_url.format(n)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find_all("td", attrs={'class': 'goodsTxtInfo'})
    imgs = soup.find_all("div", attrs={'class': 'goodsImgW'})

    for row,img in zip(table,imgs):
        p = row.select_one('p > a')
        element = row.select_one('div.aupu > a[target=_blank]')
        m = row.select_one('span.priceB')
        img_url = img.find('img')['src']
        print('URL:', img_url)
        print('제목:', p.get_text())
        if element:
            text = element.text
            print('작가:', text)
        else:
            div_element = row.select_one('div.aupu')
            if div_element:
                text = div_element.text
                print('작가:', text)
            
        print('가격:', m.get_text())
    
    

        
        
