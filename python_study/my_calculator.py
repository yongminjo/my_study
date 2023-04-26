# 계산기 만들기
# 기능 : 두 정수의 사칙연산(+, -, *, /)
# add(), sub(), mul(), div() 함수 정의
# input() 함수를 활용하여 정수 2개, 사칙연산 선택을 입력 받을 후
# 계산 결과를 print한다.
# 계산식과 결과를 calculator_result.txt파일에 기록한다.
# 사용자가 'q'를 입력하면 종료한다.

# while True:
#     print("""
#     계산기
#     1: +
#     2: -
#     3: *
#     4: /
#     q: 종료
#     """)
#     operator = input("원하는 계산을 입력하세요: ")
#     if operator == 'q':
#         break
#     a = int(input("정수 1: "))
#     b = int(input("정수 2: "))
#     def add(a, b):
#         result = "%d + %d = %d" % (a, b, a+b) # 포맷 코드 사용(정수형)예제
#         with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
#             f.write(result)

#     def sub(a, b):
#         result = f"{a} - {b} = {a-b}" # f-string 사용 예제
#         with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
#             f.write(result)

#     def mul(a, b):
#         result = str(a)+" * "+str(b)+" = "+str(a*b)
#         with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
#             f.write(result)

#     def div(a, b):
#         result = str(a)+" / "+str(b)+" = "+str(a/b)
#         with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
#             f.write(result)

#     if operator == "1":
#         add(a, b)
#         print(a,"+",b,"=",a+b)
#     elif operator == "2":
#         sub(a, b)
#         print(a,"-",b,"=",a-b)
#     elif operator == "3":
#         mul(a, b)
#         print(a,"*",b,"=",a*b)
#     elif operator == "4":
#         div(a, b)
#         print(a,"/",b,"=",a/b)


# MyCalculator 클래스로 만들어보세요.
# add, sub, mul, div 메소드


class MyCalculator:
    def __init__(self):
        pass
    def add(self, n1, n2):
        print(f"{n1} + {n2} = {n1 + n2}")

    def sub(self, n1, n2):
        print(f"{n1} - {n2} = {n1 - n2}")

    def mul(self, n1, n2):
        print(f"{n1} * {n2} = {n1 * n2}")

    def div(self, n1, n2):
        print(f"{n1} / {n2} = {n1 / n2}")

my_calculator = MyCalculator()
if __name__ == "__main__":
    while True:
        print("""
            계산기
        -------------
        1 : + (더하기)
        2 : - (빼기)
        3 : * (곱하기)
        4 : / (나누기)
        --------------
        q : 계산기 종료
        """)
        operator = input("원하는 메뉴를 입력하세요.")
        if operator == 'q':
            print("계산기를 종료합니다.")
            break
        n1 = int(input("계산할 정수 1을 입력하세요."))
        n2 = int(input("계산할 정수 2를 입력하세요."))
        if operator == "1":
            my_calculator.add(n1, n2)
        elif operator == "2":
            my_calculator.sub(n1, n2)
        elif operator == "3":
            my_calculator.mul(n1, n2)
        elif operator == "4":
            my_calculator.div(n1, n2)
        else:
            print("잘못 입력했습니다. 다시 입력하세요.")
