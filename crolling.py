from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re 

url = "https://www.yes24.com/24/category/bestseller"

driver = webdriver.Chrome()
driver.get(url)
soup = BeautifulSoup(driver.page_source,"lxml")



title = soup.find_all("li",attrs={"class":re.compile("^num")})
images = soup.find_all("p", attrs={"class": "image"})


        
for idx,titles in enumerate(title):
    
    a = titles.find("p",class_=False).get_text()
    b = titles.find("a",attrs={"target":"_blank"}).get_text()
    p = titles.find("strong").get_text()
    img_tag = titles.find("img")
    if img_tag and "src" in img_tag.attrs:
            img_url = img_tag["src"]
            response = requests.get(img_url)
            if response.status_code == 200:
                
                with open(f"movie{idx+1}.jpg", "wb") as f:
                    f.write(response.content)
                if idx >= 40 : 
                    break 
                print(f"Saved image {idx+1}")
            else:
                print(f"Failed to retrieve image {idx+1}")
    print("제목:",a)
    print("작가:",b)
    print("가격:",p)
    
