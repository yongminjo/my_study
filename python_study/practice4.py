# 다음 함수를 정의하세요.
# 정수 n을 입력받고, n보다 작은 수 중 3의 배수와 5의 배수를 모두 더한 합을 
# 반환하는 함수
# 함수 이름은 : sum_3_5

# def sum_3_5(n):       # ★ 다시 풀어보기
#     result = 0
#     for i in range(1, n):
#         if i % 3 == 0 or i % 5 == 0:
#             result += i
#     return result

# print(sum_3_5(9))

# def sum_3_5(n):
#     result = 0
#     for i in range(n):
#         if i % 3 == 0:
#             result += i
#         elif i % 5 == 0:
#             result += i
#     return result

# 정육면체 주사위 2개가 있다.
# 2개의 주사위를 던졌을 때 나올 수 있는 주사위 눈의 조합을
# 모두 print하는 함수를 정의하세요.
# 함수 이름 : draw_dice
# 출력 예시 
# 1, 2 / 6, 3

# def double_dice():
#     for i in range(1, 7):
#         for j in range(1, 7):
#             print(i, j)

# def double_dice():
#     i = 1
#     while i < 7:
#         j = 1
#         while j < 7:
#             print(i, j)
#             j += 1
#         i += 1
# double_dice()

# 두 수의 차이를 구하는 함수
# 함수에 입력된 두 정수의 차이를 계산하고 반환하는 함수를 정의하세요.
# 함수 이름 : get_diff

# def get_diff(a, b):
#     result = abs(a - b)
#     return result

#     if a > b :                 # 다른 방법으로.
#         result = a - b
#     else:
#         result = b - a
#     return result

# print(get_diff(895 , 999))

# 가장 큰 수를 만드는 함수
# 함수에 입력된 5개 정수(0 ~ 9, 중복 가능)를 사용하여 만들 수 있는
# 가장 큰 수를 반환하는 함수를 정의하세요.
# 함수 이름 : get_biggest

# def get_biggest(a, b, c, d, e):
#     numbers = [a, b, c, d, e]
#     numbers.sort()
#     result = 0
#     for i in range(len(numbers)):
#         result += numbers[i] * (10 ** i)
#     return result

    # numbers = [a, b, c, d, e]
    # numbers.sort(reverse=True)
    # result = ""
    # for i in numbers:
    #     result += str(i)
    # return int(result)

# print(get_biggest(3,5,7,2,5))

# 별 찍기 2
# 정수를 함수에 입력하여 호출하면 해당 정수 줄의 별을 화면에 출력한다.
# 함수 이름 : print_stars2


# def print_stars2(n):
#     for i in range(1, n+1):
#         print(" " * (n - i) + "★" * i)

# print_stars2(18)

