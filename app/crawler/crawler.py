from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import random

options = Options()

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)

store_url = "https://smartstore.naver.com/llovve17"

driver.get(store_url)
time.sleep(random.uniform(1.5, 3.5))

"""
category_with_subs = driver.find_elements(By.CLASS_NAME, "_3HQCww4jR6._27UBX4PJLi._nlog_click._nlog_impression_element")

category_links = []
for category in category_with_subs:
    link = category.get_attribute("href")
    if link:
        category_links.append(link)
print(category_links)
"""

category_links = [
    "https://smartstore.naver.com/llovve17/category/24590cd21ee940e7b8ecfa075cccf377?cp=1", # 배드민턴화-미즈노
    "https://smartstore.naver.com/llovve17/category/287fb55f2674469f85c3712af3cde030?cp=1", # 배드민턴화-테크니스트
    "https://smartstore.naver.com/llovve17/category/aff346e37ed84ee0973c1fffd06edd38?cp=1", # 배드민턴화-라이더
    "https://smartstore.naver.com/llovve17/category/570b985451154e1e849f171a1629cf9a?cp=1", # 배드민턴화-플로먼트
    #TODO
]

for category_link in category_links:
    driver.get(category_link)
    time.sleep(random.uniform(1.5, 3.5))

    product_list_box = driver.find_element(By.CLASS_NAME, "wOWfwtMC_3.FR2H3hWxUo")
    
    product_boxes = product_list_box.find_elements(By.CLASS_NAME, "_2id8yXpK_k.linkAnchor._nlog_click._nlog_impression_element")

    for product_box in product_boxes:
        
        product_image = product_box.find_element(By.CLASS_NAME, "_25CKxIKjAk").get_attribute("src") #TODO
        print("이미지링크: ", product_image)
        
        try:
            discount_rate = product_box.find_element(By.CLASS_NAME, "GGHHWiSIdf")
            print("할인율: ", discount_rate.text.split('%')[0])
        except:
            print("No discount")

        discount_price = product_box.find_element(By.CLASS_NAME, "zOuEHIx8DC")
        print("할인가격: ", discount_price.text.split('원')[0])

        try:
            whole_price = product_box.find_element(By.CLASS_NAME, "_29otVMEvsN")
            print("원가: ", whole_price.text.split('\n')[1][:-1])
        except:
            print("No discount")
        
        name = product_box.find_element(By.CLASS_NAME, "_26YxgX-Nu5")
        print("상품명: ", name.text)

        print('\n')

driver.quit()