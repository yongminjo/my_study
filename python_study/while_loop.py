# while 반복문
"""
while 조건:
    반복할 코드
"""
# 조건이 참인 경우에 코드를 계속 반복
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# n = 1
# while n <= 1000:
#     print(n)
#     n += 1   # n = n+1

# += 연산자
# 대입 연산자의 일종
# 더하기 연산 후 할당
# n += 1은 n = n+1이라는 의미 
# -= 빼기 연산 후 할당
# *= 곱하기 연산 후 할당
# /= 나누기 연산 후 할당
# **= 제곱 연산 후 할당
# //= 목 연산 후 할당
# %= 나머지 연산 후 할당

s1 = "안녕"
s1 += "하세요" #s1 = s1 + "하세요"

# while 반복문을 이용하여
# 10부터 1까지 순서대로 출력하세요.

# n = 10
# while n >= 1:  # while n > 0
#     print(n)
#     n -= 1

# money = 10000
# price = 1000
# coffee = 5
# while money >= price: # while money - price >= 0:
#     print("커피를 구매했습니다.")
#     money -= price
#     coffee -= 1
#     print("남은 커피 :", coffee)
#     if coffee == 0:
#         break

# break
# 반복문을 즉시 종료한다.

# while 반복문을 활용하여
# 1부터 10까지 홀수만 출력한다.

# a = 1
# while a <= 10:
#     if a % 2 == 1:
#         print(a)
#     a += 1       # 들여쓰기 주의! (들여쓸경우 실행이 제대로 안됨.)

# continue
# while 반복문의 제일 처음으로 돌아감.
# b = 0
# while b <= 9:
#     b += 1
#     if b % 2 == 0:
#         continue
#     print(b)

# 무한 반복문
# 무한 루프
# 조건식에 True를 입력해 항상 참이 되도록 하여 무한히 반복하게 한다.
# while True:
#     user_input = input("종료하려면 1을 입력해주세요.")
#     if user_input == "1":
#         break

# 무한반복문으로 계산기 만들기
# +, -, *, / 계산
# 2개의 수를 계산 a + b
# while True:
#     print("""
#          계산기
#     ===============
#     1. 더하기 (+)
#     2. 빼기 (-)
#     3. 곱하기 (*)
#     4. 나누기 (/) 
#     ===============
#     q. 나가기 (Exit)
#     """)
#     operator = input("계산 또는 메뉴를 선택하세요 : ")
#     if operator == "1":
#         print(int(input()) + int(input())) 

#     if operator == "2":
#         print(int(input()) - int(input()))

#     if operator == "3":
#         print(int(input()) * int(input()))
        
#     if operator == "4":
#         print(int(input()) / int(input()))

#     if operator == "q":
#         print("계산기를 종료합니다.")
#         break

# 코드를 수정해서 사용자가 입력한 숫자를
# 계산하도록 변경하시오.

# while True:
#     print("""
#          계산기
#     ===============
#     1. 더하기 (+)
#     2. 빼기 (-)
#     3. 곱하기 (*)
#     4. 나누기 (/) 
#     ===============
#     q. 나가기 (Exit)
#     """)
#     operator = input("계산 또는 메뉴를 선택하세요 : ")

#     if operator == "1":
#         a = int(input("더할 숫자를 입력하세요."))
#         b = int(input("더할 숫자를 입력하세요."))
#         print(a, "+", b, "=", a + b) 

#     elif operator == "2":
#         a = int(input("뺄 숫자를 입력하세요."))
#         b = int(input("뺄 숫자를 입력하세요."))
#         print(a, "-", b, "=", a - b)

#     elif operator == "3":
#         a = int(input("곱할 숫자를 입력하세요."))
#         b = int(input("곱할 숫자를 입력하세요."))
#         print(a, "*", b, "=", a * b)
        
#     elif operator == "4":
#         a = int(input("나눌 숫자를 입력하세요."))
#         b = int(input("나눌 숫자를 입력하세요."))
#         print(a, "/", b, "=", a / b)

#     elif operator == "q":
#         print("계산기를 종료합니다.")
#         break

# 사용자가 가지고 있는 돈을 입력받는다.
# 구매할 수 있는 커피의 개수와 잔돈을 출력한다.
# 구매할 수 있는 음료수의 개수와 잔돈을 출력한다.
# 구매할 수 있는 콜라의 개수와 잔돈을 출력한다.
# 커피는 500원 음료수는 700원 콜라는 930원
# 물품의 갯수는 무한하다고 가정한다.
# while 반복문을 사용하여 작성한다. (리스트도 사용)

# idx = 0
# prices = [500, 700, 930]
# money = int(input("돈:"))
# while idx <= len(prices):  # idx < 3
#     price = prices[idx]
#     print(money // price)
#     print(money % price)
#     idx += 1


# while 반복문을 사용해서
# scores 리스트에 시험 점수 5개를
# 정수형으로 입력받으세요. append, int, input 사용

# scores = []
# idx = 0
# while idx < 5:
#     scores.append(int(input("시험 점수를 입력하세요.")))
#     idx += 1
#     print(scores) # 들여쓰기 구분 잘 하자!!

# while 반복문을 사용하여 
# 구구단 2단을 출력하세요.

num = int(input("원하는 단수를 입력하세요."))
a = 1
while a <= 9:
    print(num, "*", a, "=", num*a)
    a += 1
