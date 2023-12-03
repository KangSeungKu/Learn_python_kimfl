import requests
from bs4 import BeautifulSoup

url = "https://naver.com"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Whale/3.23.214.10 Safari/537.36"
}

req = requests.get(url, headers=headers)

print(req.request.headers)

html = req.text

# print(html)

soup = BeautifulSoup(html, "html.parser")

logo = soup.select_one(".tit").text

print(logo) # 최근 검색어


# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Whale/3.23.214.10 Safari/537.36