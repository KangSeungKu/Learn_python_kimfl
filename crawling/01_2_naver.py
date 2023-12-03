import requests
from bs4 import BeautifulSoup

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
keyword = input("검색어를 입력하세요 : ")

url = base_url + keyword
print(url)

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Whale/3.23.214.10 Safari/537.36"
}

req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

# title_link _cross_trigger

# select_one은 하나의 결과만 가져옴
# select는 모든 것을 가져옴
results = soup.select(".title_link._cross_trigger")
names = soup.select(".name");

# for result in results:
#     print(result.text)  # mark 태그도 없애줌.
#     print()

for data in zip(results, names):
    print(data[1].text)
    print(data[0].text)
    print(data[0]["href"])
    print()