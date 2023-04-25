# 파일 입출력
# 파이썬에서 파일 생성, 수정


# open()
# 파이썬 내장 함수 
# 파일을 열고, 파일 객체를 리턴한다. (파이썬에서 '파일 입출력'이라고 한다)
# 사용 방법 : open(파일 이름, 파일 열기 모드)
# f = open("C:/Users/405/my_study/python_study/새파일.txt", 'w')
# f.close() # 이걸 꼭! 해줘야 한다.
# 파일의 경로
# 절대 경로 : C:/ D:/ 처럼 최상단 경로부터 나타낸 경로 (ex) 길을 물어볼때 "인천시 서구 연희동...")
# 상대 경로 : 현재 작업 위치부터 나타낸 경로 (ex) 서구청역 2번출구 100m 앞이야~~)

# 파일 열기 모드
# r : 읽기 모드. 파일을 읽기만 할 때 사용
# w : 쓰기 모드. 파일에 내용을 쓸 때 사용
# a : 추가 모드. 파일의 마지막에 새로운 내용을 추가할 때 사용

# f = open("python_study/새파일.txt", 'w', encoding="utf-8")i
# for i in range(1, 11):
#     print(i, "번째 줄")  # 터미널에만 출력
#     f.write(str(i)+"번째 줄\n") # 파일에 작성
# f.close()
# w 모드는 덮어쓰기 된다. / 새롭게 수정한 내용으로 전체 덮어쓰기
# 이는 코드를 실행할 때 마다 새롭게 작성된것이나 마찬가지.

# f = open("python_study/새파일.txt", 'a', encoding="utf-8")
# for i in range(11, 21):
#     print(i, "번째 줄")
#     f.write(str(i)+"번째 줄\n")
# f.close()
# W모드와는 다르게 a모드에서는 기존 내용을 유지하면서 덧붙이는 것.

# readline() 함수
# 첫번째 줄부터 1줄 읽어온다.
# 커서가 이동하는 것처럼 읽어옴
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# while True:
#     line = f.readline()
#     if line == "":
#         break
#     print(line)
# f.close()

# readlines() 함수
# 파일의 모든 줄을 읽어서 리스트로 반환
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# read() 함수
# 파일 내용 전체를 문자열로 리턴한다.
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# data = f.read()
# print(data)
# f.close()

# for문으로 읽기
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# for line in f:
#     print(line)
# f.close()   # readline 방식처럼 동작.

# with문
# open - close를 자동으로 해준다. (코드 실행하는 동안만 open.)
# with open("python_study/새파일.txt", 'a', encoding="utf-8") as f:
#     f.write("end of file") 
#     f.write("2")
#     f.write("3")
#     f.write("4")# 이 코드 실행 후 중단.
# f.write("5") # 이 코드는 실행하지 않는다.

# csv(comma separated values)
# ,로 구분되는 값을 모아놓은 파일 (보통은 ,로 구분하지만 데이터에 따라 tap도있음.)
# ex) 이름, 입실시간, 퇴실시간
# ex) 조용민, 09:20, 18:10
# with open("python_study/data.csv", "w", encoding="utf-8") as f:
#     f.write("날짜,날씨,기온\n")
#     f.write("20230424,맑음,10\n")
#     f.write("20230425,비,9\n")

# with open("python_study/data.csv", "r", encoding="utf-8") as f:
#     data = f.readlines()
#     print(data)

# 계산 결과 저장 함수
# 정수 2개를 입력받고 두 수를 더한 결과를 add_result.txt 파일에
# 저장하는 함수를 정의하세요.
# 함수 이름 add_write

# def add_write(n1,n2):
#     result = n1 + n2
#     with open("add_result.txt","w",encoding="utf-8") as f:
#         f.write(str(result))
    
# add_write(34,35)

# 텍스트 파일에 적힌 정수 2개를 읽어와서 더하는 함수를 정의하세요.
# 텍스트 파일 이름 : add_number.txt
# 경로 : python_study/add_number.txt
# 정수 2개를 더한 결과를 print 하세요.
# 함수 이름 : read_add_print

# def read_add_print():
#     with open("python_study/add_number.txt", "r", encoding="utf-8") as f:
#         data = f.read()
#         a = int(data[0])
#         b = int(data[2])
#         print(a + b)

# read_add_print()
