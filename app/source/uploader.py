import os
import re

import requests
import pandas as pd
from boto3 import client
from dotenv import load_dotenv

load_dotenv()

bucket_name = os.environ.get("S3_BUCKET_NAME")
local_file_path = "test.jpg"
s3 = client("s3")

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

    image = requests.get(image_url)

    with open(local_file_path, "wb") as f:
        f.write(image.content)

    s3_file_name = f"products/{name_sanitized}/thumbnail.jpg"
    s3.upload_file(local_file_path, bucket_name, s3_file_name)