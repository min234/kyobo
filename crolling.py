import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://www.yes24.com/Main/default.aspx"
service1 = Service(executable_path='C:/project/dd/chromedriver.exe')

driver = webdriver.Chrome(service=service1)
driver.get(base_url)

wait = WebDriverWait(driver, 40)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="LoginText"]/a/em')))
element.click()

id_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SMemberID"]')))
id_element.send_keys('ektmd7676')

password_element = driver.find_element(By.XPATH, '//*[@id="SMemberPassword"]')
password_element.send_keys('alsdnr7676!')

element3 = driver.find_element(By.XPATH, '//*[@id="btnLogin"]/span')
element3.click()

time.sleep(5)

best = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yesFixCorner"]/dl/dd/ul[1]/li[1]/a')))
best.click()


for i in range(1, 41): 
    co = driver.find_elements(By.CLASS_NAME, 'num{}'.format(i))

    for cos in co:
        a = cos.find_elements(By.CSS_SELECTOR, 'p a')
        price = cos.find_element(By.TAG_NAME, 'strong')
        if len(a) > 2:
            c = a[2]
            d = a[3]

            print('번호:', i)
            print('제목:', c.text)
            print('작가:', d.text)
            print('가격:', price.text)
            time.sleep(2)

            c.click()

            time.sleep(2)
            elements = driver.find_elements(By.XPATH, '//*[@id="infoset_specific"]/div[2]/div/table/tbody/tr')

            for element in elements:
                tds = element.find_elements(By.XPATH, './td')
                for td in tds:
                    print('품목정보:', td.text)

            
            time.sleep(2) 
            driver.back()
            
            if i == 40:
                add = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bestList"]/p[2]/a/img')))
                add.click()

                while True:
                    for i in range(1, 80, 2):
                        names = driver.find_elements(By.XPATH, f'//*[@id="category_layout"]/tbody/tr[{i}]')

                        for ttdss in names:
                            name1 = ttdss.find_element(By.CLASS_NAME, 'goodsTxtInfo')
                            num = ttdss.find_element(By.CLASS_NAME,'num')
                            name = name1.find_element(By.CSS_SELECTOR, 'p a')
                            at = ttdss.find_element(By.CLASS_NAME, 'aupu')
                            pp = ttdss.find_element(By.CLASS_NAME, 'priceB')

                            print('번호:', num.text)
                            print('제목:', name.text)
                            print('작가:', at.text)
                            print('가격:', pp.text)

                            time.sleep(2)

                            name.click()

                            time.sleep(2)

                            elements = driver.find_elements(By.XPATH, '//*[@id="infoset_specific"]/div[2]/div/table/tbody/tr')

                            if elements:
                                for element in elements:
                                    tds = element.find_elements(By.XPATH, './td')
                                    for td in tds:
                                        print('품목정보:', td.text)

                            driver.back()
                            time.sleep(2)

                        if i == 79:
                            p_tag = driver.find_element(By.XPATH, '//*[@id="bestList"]/div[3]/div[1]/div[1]/p')

                            all = p_tag.find_elements(By.XPATH, './*') 

                            for index, alls in enumerate(all, start=1):
                                tag = alls.tag_name
                                
                                
                                if tag == 'strong' and index < len(all):
                                    next = all[index]
                                    if next.tag_name == 'a':
                                        time.sleep(2)
                                        next.click()  
                                        break
            

