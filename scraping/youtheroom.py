import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.youtheroom2

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://www.youtheroom.kr/product/list.php?ca_id=10&page=2&sort1=&sort2=&status=end&search=&page=3', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.content.decode("utf-8", 'replace'), 'html.parser')

# select를 이용해서, tr들을 불러오기
programs = soup.select('#gallery_Card_Wrap > ul > li ')

for program in programs:
    link = program.select_one("a")["href"]
    img = program.select_one("a > div.gallery_Card_img > img")["src"]
    title = program.select_one('a > div > h4')
    em = program.select_one('a > div.gallery_Card_info >div.gallery_close_mob > em').text
    p = program.select_one('a > div.gallery_Card_info >div.gallery_close_mob > p ').text

    if title is not None:
        print("http://www.youtheroom.kr/product/" + link)
        print("http://www.youtheroom.kr" + img)
        print(title.text, p, em[0:4])
        print()

        doc = {
            'link': "http://www.youtheroom.kr/product/" +link,
            'img': "http://www.youtheroom.kr" +img,
            'title': title.text,
            'duration': p,
            'status': em[0:2]
        }
        db.programs.insert_one(doc)
