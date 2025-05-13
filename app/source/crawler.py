import time
import random

import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

options = Options()

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)

"""
store_url = "https://smartstore.naver.com/llovve17"

driver.get(store_url)
time.sleep(random.uniform(1.5, 3.5))

category_with_subs = driver.find_elements(By.CLASS_NAME, "_3HQCww4jR6._27UBX4PJLi._nlog_click._nlog_impression_element")

category_links = []
for category in category_with_subs:
    link = category.get_attribute("href")
    if link:
        category_links.append(link)
print(category_links)
"""

category_links = {
    "신발-미즈노": "https://smartstore.naver.com/llovve17/category/24590cd21ee940e7b8ecfa075cccf377?cp=1",
    "신발-테크니스트": "https://smartstore.naver.com/llovve17/category/287fb55f2674469f85c3712af3cde030?cp=1",
    "신발-라이더": "https://smartstore.naver.com/llovve17/category/aff346e37ed84ee0973c1fffd06edd38?cp=1",
    "신발-플로먼트": "https://smartstore.naver.com/llovve17/category/570b985451154e1e849f171a1629cf9a?cp=1",
    "라켓-미즈노": "https://smartstore.naver.com/llovve17/category/c41e87a4b79e47a9ab1daad3a23c3d6b?cp=1",
    "라켓-테크니스트": "https://smartstore.naver.com/llovve17/category/dbcacd996b284352a8a3b7d1358cab91?cp=1",
    "라켓-컨트롤마스터": "https://smartstore.naver.com/llovve17/category/f3a1724a1b4c412fb931db98d8153054?cp=1",
    "라켓-레드썬": "https://smartstore.naver.com/llovve17/category/56e62f837e204ad2bf3a1373945e4311?cp=1",
    "라켓-트라이온": "https://smartstore.naver.com/llovve17/category/567069cafccc486480fca1902f80e721?cp=1",
    "배드민턴의류-테크니스트": "https://smartstore.naver.com/llovve17/category/bc79db3e794147a197d177f3246efad2?cp=1",
    "배드민턴의류-라이더": "https://smartstore.naver.com/llovve17/category/ead63a6bc3be4047b9005e8320f247da?cp=1",
    "배드민턴의류-트라이온": "https://smartstore.naver.com/llovve17/category/5c072dc41acb4d2ca965684132c7c8b5?cp=1",
    "배드민턴의류-핏섬": "https://smartstore.naver.com/llovve17/category/45532fed2eac4dc297bd2506fa390efd?cp=1",
    "배드민턴의류-컨트롤마스터": "https://smartstore.naver.com/llovve17/category/4a6924b3cbe64a328dac5da7b0b306de?cp=1",
    "배드민턴의류-미즈노": "https://smartstore.naver.com/llovve17/category/4608fcfb1e054976bc031bb3fc3998da?cp=1",
    "배드민턴의류-트리코어": "https://smartstore.naver.com/llovve17/category/0c3e00b20e4c41fca9499f9cb0db430f?cp=1",
    "배드민턴의류-스펙트럼": "https://smartstore.naver.com/llovve17/category/bbc580b9c5b749b3aa581a403086ac6c?cp=1",
    "배드민턴의류-스포츠베어": "https://smartstore.naver.com/llovve17/category/a5b10fd5f1cb41d28edcebbf408553cd?cp=1",
    "배드민턴가방-라이더": "https://smartstore.naver.com/llovve17/category/7b9af7a6e34b4af0acb5a0d550029e90?cp=1",
    "배드민턴가방-테크니스트": "https://smartstore.naver.com/llovve17/category/9a765f00f1c24dfaad4e42e01280dfbc?cp=1",
    "배드민턴가방-미즈노": "https://smartstore.naver.com/llovve17/category/96737855b22a428182e752a2be966b87?cp=1",
    "배드민턴가방-트라이온": "https://smartstore.naver.com/llovve17/category/3763caec70eb4acb80664e2f1fc9aeb0?cp=1",
    "배드민턴가방-레드썬": "https://smartstore.naver.com/llovve17/category/0daa8dd0d0ee4d2292c073c7b54d50a0?cp=1",
    "배드민턴가방-컨트롤마스터": "https://smartstore.naver.com/llovve17/category/d161c08c44b64c1dbd631bd031c77a21?cp=1",
    "배드민턴가방-핏섬": "https://smartstore.naver.com/llovve17/category/8a7f7bcff99040d2b52c327cf5a36db2?cp=1",
}

product_data = []

for category, category_link in category_links.items():
    driver.get(category_link)
    time.sleep(random.uniform(1.5, 3.5))
    
    category_first = category.split('-')[0]
    category_second = category.split('-')[1]

    try:
        product_list_box = driver.find_element(By.CLASS_NAME, "wOWfwtMC_3.FR2H3hWxUo")
    except:
        try:
            product_list_box = driver.find_element(By.CLASS_NAME, "wOWfwtMC_3._3cLKMqI7mI")
        except:
            print("NO PRODUCT_LIST_BOX")
            continue
    
    product_boxes = product_list_box.find_elements(By.CLASS_NAME, "_2id8yXpK_k.linkAnchor._nlog_click._nlog_impression_element")

    for product_box in product_boxes:
        product_image = product_box.find_element(By.CLASS_NAME, "_25CKxIKjAk").get_attribute("src")
        print("대표이미지링크: ", product_image)

        try:
            discount_rate = product_box.find_element(By.CLASS_NAME, "GGHHWiSIdf").text.split('%')[0]
            print("할인율: ", discount_rate)
        except:
            discount_rate = 0
            print("No discount")
        
        discount_price = product_box.find_element(By.CLASS_NAME, "zOuEHIx8DC").text.split('원')[0]
        print("판매가: ", discount_price)
        
        try:
            whole_price = product_box.find_element(By.CLASS_NAME, "_29otVMEvsN").text.split('\n')[1][:-1]
            print("원가: ", whole_price)
        except:
            whole_price = 0
            print("No discount")
        
        name = product_box.find_element(By.CLASS_NAME, "_26YxgX-Nu5").text
        print("상품명: ", name)

        product_info_link = product_box.get_attribute("href")
        print("상세링크: ", product_info_link)

        print('\n')

        product_data.append({
            "대분류": category_first,
            "소분류": category_second,
            "상품명": name,
            "대표이미지링크": product_image,
            "할인율(%)": discount_rate,
            "판매가(원)": discount_price,
            "원가(원)": whole_price,
        })

df = pd.DataFrame(product_data)
df.to_csv("naver_smartstore_products.csv", index=False, encoding="utf-8-sig")

driver.quit()