# function 함수
# 입력 -> 처리 -> 출력
# input(입력)을 받아서 특정 작업(처리)을 수행하고 output(출력)을 반환한다.

# 내장 함수(built-in)
# 파이썬이 기본적으로 제공해주는 함수
# print()
# len()
# zip()
# int()
# float()
# str()
# list()
# range()

# abs(값)
# absolute의 약자
# 입력한 숫자형 데이터의 절댓값을 반환한다.
# print(abs(100)) -> 100
# print(abs(-100)) -> 100
# print(abs(3.15)) -> 3.15
# print(abs(-3.15)) -> 3.15

# sum(리스트)
# 리스트 안의 숫자를 모두 더한 값을 반환한다.
# print(sum([1, 2, 3, 4, 5])) -> 15

# max(리스트)
# 리스트 안에서 최댓값을 찾아 반환한다.
# print(max([1, 2, 3, 4, 5])) -> 5

# min(리스트)
# 리스트에서 최솟값을 찾아 반환한다.
# print(min([1, 2, 3, 4, 5])) -> 1
# .min()과는 다름

# chr(정수)
# 정수를 입력받고 해당하는 유니코드 문자를 반환한다.
# print(chr(65)) -> A

# ord(문자)
# 문자 1개를 입력받고 해당하는 정수를 반환한다.
# print(ord('A')) -> 65

# chr(정수) 와 ord(문자)는 세트!!

# round(값) 
# round(값, 소수 자릿수)
# 반올림 함수
# print(round(1.234))  -> 1
# print(round(1.234, 2))  -> 1.23
# print(round(1.369, 1))  -> 1.4 

# 함수 정의(define)
# 함수 이름
# 함수 입력값 parameter
# 함수 결괏값 return value
"""
def 함수 이름 (함수입력값):
    함수기능코드
    return (함수 결괏값)
"""
# def => 함수를 정의하는 명령어
# 함수이름도 변수 이름처럼 규칙을 지켜서 지어야한다. 
# 영어, 숫자, _만 사용
# 숫자 시작, 띄어쓰기, 키워드 사용하면 안됨.
# 기존에 이미 정의된 함수 이름도 피하는 것이 좋음 (덮어씌워짐)

# def print_names():
#     print("손흥민")
#     print("황희찬")
#     print("김민재")
#     print("이강인")

# # print_names()

# def get_name():
#     return "조용민"

# def print_my_name():
#     print(get_name())

# print_my_name()
# a = print_names() # 리턴이 없음 
# b = get_name() # 리턴이 있음

# print(a)
# print(b)

# parameter
# 함수에 입력하는 값
# 매개변수, argument, 인수, 인자 혼용 (엄밀히 말하면 parameter가 맞음) 
# def add(a, b):
#     return a + b

# def print_add(a, b):
#     print(a + b)

# result = add(1, 2)
# print(result)

# # print_add(1, 2)
# result = print_add(1, 2)
# # print(result)

# print_add("안녕", "하세요") # 안녕하세요 -> 문자형과 문자형은 더해진다.(이어진다.)
# print_add("안녕", 1) # 에러가 난다. (문자형과 숫자형은 더할 수 없음)
# print_add(b="하세요", a="안녕") # 안녕하세요 -> 매개변수를 지정해서 함수를 호출할 수 있음

# def swap_number(a, b):
#     temp = a
#     a = b
#     b = temp
#     print(a, b) # 지역 변수 (Local variable)
#     return a, b

# a = 1  # 전역 변수 (Global variable)
# b = 2
# print("함수 호출 전", a, b) # = 함수 호출 전 1 2
# a, b = swap_number(a, b) 
# print("함수 호출 후", a, b) # = 함수 호출 후 2 1

# 다음 함수를 정의하세요.
# 함수 이름 : mul
# 함수 입력값 : 정수 2개
# 함수 출력값 : 정수 2개의 곱

# def mul(a, b): 
#     return a * b

# print(mul(3, 4))

# result = mul(3, 4)
# print(result)

# a = 1
# b = 2
# c = 3
# a, b, c = 1, 2, 3
# d, e, f = [4, 5, 6]
# g, h, i = (7, 8, 9)

# 기본 값 매개변수
# default value parameter 
# 함수 호출 시 n2에 입력된 값이 없으면 기본 값 사용
# def mul(n1, n2=1):
#     return n1 * n2

# mul(1, 2) => 1 * 2 = 2
# mul(1) => 1 * 1(기본값) = 1

# def test_func(x, test=[]): # 리스트를 기본값으로 사용하면 값이 누적됨.(리스트 사용 X)
#     test.append(x)         # mutable한 값이여서 누적.
#     print(x, test)

# test_func(1)
# test_func(2)

# def test_func1(x, test=5):
#     test = test
#     print(x, test)

# test_func1(1)
# test_func1(2)

# def test_func2(x, test=None): # 빈 리스트를 궂이 추가하려고 할 때.
#     if test == None:
#         test = []
#     test.append(x)
#     print(x, test)  # 결론, 리스트는 기본값으로 추가하는 건 좋지 않다.

# def sub(n1, n2, n3=0): # 기본값이 있는 매개변수는 기본값이 매개변수보다 뒤에 위치해야 함
#     print(n1 - n2 - n3)

# 1 ~ 10까지 더한다
# *를 사용한 매개변수 -> 입력값이 몇개가 될지 모를 때(안정해졌을때) 사용
# add_many(1,2) -> 3
# # add_many(1,2,3,4,5) -> 15
# def add_many(*args):
#     # 튜플처럼 사용
#     # 인덱싱, 슬라이싱 사용 가능
#     result = 0
#     for i in args:
#         result += i
#     return result

# result1 = add_many(1,2,3,4,5)
# print(result1)
# result2 = add_many(3,2,5,9,1)
# print(result2)
# result3 = add_many(1,2)
# print(result3)

# def calc_many(n1, *args):
#     result = n1
#     for i in args:
#         result += i
#     return n1

# 키워드 매개변수
# **kwargs
# keyword arguments
# 딕셔너리로 사용
# def print_kwargs(**kwargs): # 들어오는 값이 유동적일 때 사용한다.
#     print(kwargs)

# print_kwargs(a=1, b=2)
# print_kwargs(name='이름', age=20) # 요즘은 파이썬에서 사용을 지양하는 추세.

# 함수의 반환
# return 반환값
# return을 만나면 반환값을 반환함과 동시에 함수가 종료된다.
# def test_func5():
#     print(1)
#     print(2)
#     print(3)
#     return None
#     print(4)
#     print(5)
# 함수의 반환값은 무조건!! 1개이다.
# def test_func6(a, b):
#     # return (a + b, a * b)
#     return a + b, a * b

# result = test_func6(1, 2)
# res_add, res_mul = test_func6(1, 2)
# res_add, res_mull = (a+b, a*b)

# 홀수 판별 함수
# 정수 1개를 입력받고 홀수인지 판별하는 함수
# 함수 이름 : is_odd_number
# 파라미터 : n
# 반환값 : 홀수면 True, 짝수면 False

# def is_odd_number(n):
#     if n % 2 == 1:
#         return True
#     else:
#         return False
    
# def is_odd_number(n):
#     if n % 2 == 1:
#         return True
#     return False

# def is_odd_number(n):
#     return n % 2 == 1   

# print(is_odd_number(2))

# 테두리를 출력하는 함수
# 문자열을 입력받고 print함수를 이용해 테두리와 함께 문자를 출력한다.
# 함수 이름 : get_bordered_str
# 파라미터 : message
# 반환값 : None
# print 예시 
"""
*****
hello
*****
"""

# def get_bordered_str(message):
#     message = str(message)
#     n = len(message) 
#     print("*" * n)
#     print(message)
#     print("*" * n)

# get_bordered_str(12345)

# 속도를 변환하는 함수
# m/s 단위의 속도가 입력되면 km/h단위의 속도로 변환한다.
# 함수 이름 : convert_velocity
# 파라미터 : velocity
# 반환값 : km/h로 변환된 속도

# def convert_velocity(velocity):
#     conv = velocity * 3.6  # 초속 * 3.6 = 시속
#     return conv

# velocity = convert_velocity(60)
# print(velocity)

"""
출력 결과 n -> 4일때
*
**
***
****
"""

# 별 찍기 함수  ★다시 풀어보기
# 정수를 함수에 입력하여 호출하면 해당 정수 줄의 별을 화면에 출력한다.
# 함수 이름 : print_stars
# 파라미터 : n
# 반환값 : None

# def print_stars(n):
#     for i in range(n): # 0 ~ n-1
#         for j in range(i+1): # 0 ~ i
#             print("*", end="")
#         print()
    
    # for i in range(0, n+1):
    #     print(i * "*")

#  