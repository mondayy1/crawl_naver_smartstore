import re
from io import BytesIO

import requests
import pandas as pd

df = pd.read_csv("naver_smartstore_products.csv")

for index, row in df.iterrows():
    category_first = row['대분류']
    category_second = row['소분류']
    name = row['상품명']
    image_url = row['대표이미지링크']
    discount_rate = row['할인율(%)']
    price_sell = row['판매가(원)']
    price_whole = row['원가(원)']

    name_sanitized = re.sub(r'\s+', '-', name.strip())

    print(category_first, category_second, name_sanitized, image_url, discount_rate, price_sell, price_whole, sep='\n')

    api_url = "http://localhost:8000/products"

    image_response = requests.get(image_url, timeout=10)
    image_bytes = image_response.content

    files = {
        "image_thumbnail": ("thumbnail.jpg", BytesIO(image_bytes), "image/jpeg"),
        "image_detail": ("detail.jpg", BytesIO(image_bytes), "image/jpeg"),
    }

    data = {
        "name": str(name_sanitized),
        "price_whole": str(int(str(price_whole).replace(",", ""))),
        "price_sell": str(int(str(price_sell).replace(",", ""))),
        "discount_rate": str(int(str(discount_rate))),
        "category_main": str(category_first),
        "category_sub": str(category_second),
    }

    product = requests.post(url=api_url, data=data, files=files)

    break