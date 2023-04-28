# 데이터 수집 단계
# 데이터 수집 -> 데이터 분석, 처리 -> 인공지능 모델 학습 -> 인공지능 모델 평가 -> 사용

# 크롤링을 하려면 알아야 할 것들
# http(hypertext transfer protocol)
# request(요청) - response(응답)
# client(웹브라우져) - server()

# html (hypertext markup language)
# 웹사이트를 표현하기 위한 언어
# <html></html>
# HTML 파싱

# import requests

# url = "https://www.naver.com/"
# response = requests.get(url)
# status = response.status_code
# html = response.text
# print(status)
# print(html)

# http 상태 코드(.status_code)
# 200 : OK(요청 성공)
# 302 : 리다이렉트(다른 페이지로 바로연결)
# 400 : Bad Request (요청이 잘못됨)
# 401 : Unauthorized (비인증됨)
# 403 : Forbidden (접근 권한 없음)
# 404 : Not found (요청받은 내용이 없음)
# 405 : Method not allowed (접근 방법이 잘못됨)
# 500 : Internal Server Error (서버 에러/개발자 문제,,,)
# 501 : Not Implemented
# 502 : Bad Gateway (잘못된 응답/서버 프로그램,,,문제)

# url 구조
# 프로토콜://호스트주소:포트번호/경로?쿼리
# http://www.naver.com/~~~? ~~~~~~~~
# 쿼리 : 추가적인 데이터 관리 / 파이썬에서 변수에 대입하듯이 'query =' 치킨 형식으로 사용
# 쿼리이름 = 값 & 쿼리이름 = 값 & 쿼리이름 = 값

# https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%B9%98%ED%82%A8
# 프로토콜   호스트주소:포트번호     경로 ?   쿼리    &   쿼리    &        쿼리(치킨)  

# search_url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
# keyword = "맥주"
# url = search_url+keyword
# response = requests.get(url)
# print(type(response.text))
# import requests
# BeautifulSoup
# html 파싱(parsing)
# html을 객체 구조화해서 사용
# from bs4 import BeautifulSoup
# html 태그
# <태그이름 속성=속성값>내용</태그이름> 
# html - head
#      - body

# search_url = "https://www.google.com/search?tbm=isch&q="
# keyword = ""
# url = search_url+keyword
# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html, "html.parser")
# imgs = soup.find_all('img')
# import os
# folder_name = "imgs"
# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)
# for idx, img in enumerate(imgs[1:]):
#     print(idx, "번째 이미지 저장")
#     file_name = f"{keyword}_{idx}.jpg"
#     file_path = os.path.join(folder_name, file_name)
#     img_response = requests.get(img['src'])
#     img_data = img_response.content
#     with open(file_path, "wb" ) as f:
#         f.write(img_data)

# enumerate(이터러블)
# li1 = ["김연아", "류현진", "손흥민"]
# for name in enumerate(li1):
#     print(name)

# 네이버 IT / 과학 뉴스 크롤륑
import os
import requests
from bs4 import BeautifulSoup
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
# headers={"User-Agent" : "Mozilla/5.0"} -->  크롤링 방지 회피! (파이썬을 봇으로 인식해서...)
response = requests.get(url, headers={"User-Agent" : "Mozilla/5.0"})
html = response.text
print(html)
soup = BeautifulSoup(html,"html.parser")
div = soup.body.find('div', attrs={'class' : 'list_body'})
headlines = div.find_all('a', attrs={'class' : 'cluster_text_headline'})
forlder_name = "crawling_result"
if not os.path.exists(forlder_name):
    os.mkdir("crawling_result")
for headline in headlines:
    # 과제 crawling_result 폴더의 headlines.txt 파일에 저장
    # print(headline.text.strip())
    # with open("crawling_result/headlines.txt", "a", encoding="utf-8") as f:
    #     f.write(headline.text.strip())
    #     f.write("\n")
    article_response = requests.get(headline['href'])
    article_soup = BeautifulSoup(article_response.text, "html.parcer")
    article = article_soup.find('div', attrs={"id":"dic_area"})
    print(article.text)