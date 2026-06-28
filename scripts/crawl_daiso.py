import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.daisomall.co.kr/ds/display/categoryList.do?dispClsCd=5000001"

def crawl_products():
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        products = []
        # (이후 코드 내용 생략 - 이전 답변의 코드를 그대로 사용하세요)
        # ... 중략 ...
        with open('products.json', 'w', encoding='utf-8') as f:
            json.dump(products, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    crawl_products()
