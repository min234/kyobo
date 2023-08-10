import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

url = 'https://www.yes24.com/24/Category/BestSeller'
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