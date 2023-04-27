# 표준 라이브러리 
# (라이브러리 = 패키지들을 모아놓은 곳)
# (모듈을 모아놓은 것(묶음) = 패키지)
# 파이썬에서 지원하는 표준 라이브러리
# 파이썬을 설치할 때 자동으로 함께 설치 
# 따로 설치하지 않고 import 명령으로 불러옴

# datetime 라이브러리
# 날짜 관련 라이브러리
# datetime의 date 객체 사용
# import datetime
# day1 = datetime.date(2023, 4, 17)
# day_end = datetime.date(2023, 9, 18)
# diff = day_end - day1
# print(diff.days)

# 2018년 8월 6일 무슨요일??
# weekday() --> 0: 월, 1:화 ~~~~~~ 6: 일
# import datetime 
# day = datetime.date(2018, 8, 6)
# weekdays = ["월", "화", "수", "목", "금", "토", "일"]
# print(weekdays[day.weekday()])

# datetime의 포맷팅 코드
# 날짜 표시하는 방법 
# 년/월/일
# 월/일/년
# 일/월/년
# 2023년 4월 27일
# 2023-04-27
# 23년 4월 27일
# import datetime
# today = datetime.datetime.today() # 시스템의 현재 날짜 및 시간이 출력된다.
# strftime()
# print(today.strftime("%Y년 %m월 %d일"))
# %Y --> 년도 (4자리 다 출력)
# %y --> 년도 (2자리 출력)
# %m --> 월 (소문자!!)
# %d --> 일
# %H --> 시간(24시간제)
# %I --> 시간(12시간제)
# %M --> 분 (대문자!!)
# %S --> 초
# %A --> 요일

# print(today.strftime("%A"))

# time 라이브러리
# 시간 관련

# import time
# time_now = time.time()
# print(time_now) # 초로 나오는데, 1970년 1월 1일부터 잰 초의 시간~~
# print(time.strftime("%H:%M:%S", time.localtime(time_now)))

# time.sleep()
# import time
# print("before")
# print("after")
# time.sleep(2) # 괄호 안의시간 (초)동안 멈췄다가 동작, 정확한 초가 아님. 근사치
# for i in range(10):
#     print(i)
#     time.sleep(0.5) # 반복작업(크롤링 등)에 유용...

# math
# 수학과 관련
# import math
# result = math.ceil(1.1)  # 올림 (실수형 -> 정수형)
# print(result)
# result = math.floor(1.9) # 버림(내림) (실수형-> 정수형)
# print(result)
# print(math.pi)

# random
# 난수 관련
# import random
# random.random()
# 0.0 ~ 1.0 사이의 실수 중 난수 값
# random_value = random.random()
# print(random_value)

# random.randint(시작, 끝)
# 시작 ~ 끝 사이의 정수 중 난수 값 
# random_value = random.randint(1, 10) #(1포함(!)~ 10포함(!))
# print(random_value)

# random.choice(리스트)
# 리스트의 요소 중 무작위로 하나를 리턴
# foods = ["서브웨이", "맥도날드", "짜장면", "국밥", "김치찌개"]
# food = random.choice(foods)
# print(food)

# li = [1, 2, 3, 4, 5]
# random.shuffle(li)
# print(li)

# lotto_numbers = list(range(1, 46))
# my_lotto = []
# for i in range(6):
#     random_value = random.choice(lotto_numbers)
#     if random_value not in my_lotto: # 포함 연산자
#         my_lotto.append(random_value)
# print(my_lotto)

# in 연산자 
# a in b 형태로 사용
# a가 b에 포함되어 있으면 True
#      "     되어 있지 않으면 False

# not in 연산자
# a not in b
# a가 b에 포함되어 있지 않으면 True
# a가 b에 포함되어 있으면 False

# li = [1, 2, 3, 4, 5]
# a = 10
# for i in li:
#     if a == i:
#         print("이미 있음")
                    # 위 아래 둘 다 똑같은 결과, 효율적인건 밑
# if a in li:
#     print("이미 있음")

# lotto_numbers = list(range(1, 46))
# random.shuffle(lotto_numbers)
# my_lotto = lotto_numbers[:6]
# print(my_lotto)

# 색 이름과 음식 이름을 합치면 멋진 밴드 이름이 된다고 한다.
# 색 이름과 음식 이름을 무작위로 뽑아
# 밴드 이름을 추천하는 프로그램을 만들어보세요.

# import random

# foods = ["와플", "샌드위치", "브로콜리", "아이스티", "커피", "와인", "롱아일랜드티", "요거트", "샐러드", "쿠키", "콜라", "사시미"]
# colors = ["베이지", "블랙", "블루", "핑크", "그레이", "다크퍼플", "딥그린", "올리브그린", "퍼플", "스카이블루", "차콜", "미드나잇블루"]

# food = random.choice(foods)
# color = random.choice(colors)

# band_name = color + food
# print(band_name)

# 숫자 야구 게임
# 1. 정답을 정한다 (4자리 숫자, 랜덤)
# 2. 게임 유저가 정답을 입력한다.
# 3. 정답과 비교해서 S / B / OUT 개수를 알려준다.
# 4. 정답을 맞추거나, 종료를 입력하면 끝난다.
# 5. 답을 맞췄을 때 "한번 더 하시겠습니까?" 메시지 띄우기

# import random
# numbers = list(range(10))
# random.shuffle(numbers)
# answer = numbers[1:5] if numbers[0] == 0 else numbers[:4]
# while True:
#     user_input = input("정답은???????????????")
#     if user_input == "종료":
#         print("종료합니다~~!!")
#         break
#     # 만약 숫자가 아닌 값이 입력->다시 입력->처음->continue
#     # isdigit() 숫자로만 이루어진 문자열인지 확인
#     # 숫자로만 이루어짐 -> T / 아니면 -> F
#     if not user_input.isdigit():
#         print("4자리 숫자만 입력하세요!")
#         continue
#     # 만약 4자리 숫자가 아니면 -> 처음으로 -> continue
#     elif len(user_input) != 4:
#         print("4자리 숫자만 입력하세요!")
#         continue
#     # 첫번째 숫자가 0일때
#     elif user_input[0] == "0":
#         print("첫번째 숫자가 0이 아닌 다른 숫자를 입력하세요")
#         continue
#     # 중복된 숫자
#     duplicate = False
#     for i in range(3):
#         if user_input[i] in user_input[i+1:]:
#             duplicate = True
#             break
#     if duplicate:
#         print("중복된 숫자가 없게 입력하세요.")
#         continue
#     strike = 0
#     ball = 0
#     out = 0
#     for i in range(4):
#         input_value = int(user_input[i])
#         if input_value not in answer:
#             out += 1
#         elif input_value == answer[i]:
#             strike += 1
#         else:
#             ball += 1    
#     print(f"strike: {strike}, ball: {ball}, out: {out}")
#     if strike == 4:
#         print("정답!")
#         user_input = input("한번 더 하시겠습니까? [y/n]")
#         if user_input ==  "y":
#             numbers = list(range(10))
#             random.shuffle(numbers)
#             answer = numbers[1:5] if numbers[0] == 0 else numbers[:4]
#         else:
#             break   
# 삼항 연산자
# (참일 때 값) if (조건) else (거짓일 때 값)
# result = "참" if True else "거짓"
# result = "참" if False else "거짓"
# print(result)

# def is_odd_number

# os
# os 자원을 제어

import os
# os.environ
# 시스템의 환경 변수 값을 리턴한다.
# print(os.environ)

# os.getcwd()
# get current working directory (현재 작업 위치를 '절대경로'로 리턴)
# print(os.getcwd())

# os.mkdir(디렉토리)
# 디렉토리(폴더)를 만든다.
# os.mkdir("폴더1")

# os.rename(원래이름, 바꿀이름)
# 파일의 이름을 바꾼다.
# os.rename("파일1", "파일2")

# os.rmdir(디렉터리)
# 디렉터리(폴더)를 지운다
# 폴더 안에 아무것도 없어야 지울 수 있다.
# os.rmdir("폴더1")

# os.unlink(파일)
# 파일을 지운다
# os.unlink("파일2")

# os.path
# os.path.exists("경로")/파일이 있는지 확인한다.
# 파일이 있으면 True, 없으면 False

# if not os.path.exists("없는파일"):
#     f = open("없는파일", "w")
#     f.close
# f = open("없는파일", "r")

# os.path.join("경로", "경로", "경로")
# 경로를 합쳐서 1개의 경로로 만들어준다.
# cwd = os.getcwd()
# my_folder = "python_study"
# file_name = "test_file.txt"
# file_path = os.path.join(cwd, my_folder, file_name)
# with open(file_path, "w", encoding="utf-/") as f:
#     f.write("테스트 파일을 작성합니다.")

#  외부 라이브러리
# 파이썬 표준 라이브러리가 아닌 라이브러리 pip를 사용해서 설치한다.
# pip(package installer for python)
# 파이썬 모듈, 패키지 설치하는 도구.
# numpy, pandas, Tensorflow, opencv, django... 등등
# PyPI(Python Package Index) 파이썬 소프트웨어 저장 공간
# PyPI에 있는 파이썬 패키지를 설치해준다.

# pip install '패키지 이름'  --> '패키지 이름' 패키지를 설치 (제일 최신버전 설치)
# pip uninstall '패키지 이름'  --> '패키지 이름' 패키지를 삭제
# pip install '패키지 이름'==1.0.5 => 버전을 명시해서 설치할 수 있다!
# pip install --upgrade '패키지 이름' --> 최신 버전으로 업그레이드
# pip list --> 설치된 패키지 리스트 확인

# pip freeze --> 설치된 패키지 목록 저장 / 배포를 쉽게 해주는것