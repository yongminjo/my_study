# 계산기 만들기
# 기능 : 두 정수의 사칙연산(+, -, *, /)
# add(), sub(), mul(), div() 함수 정의
# input() 함수를 활용하여 정수 2개, 사칙연산 선택을 입력 받을 후
# 계산 결과를 print한다.
# 계산식과 결과를 calculator_result.txt파일에 기록한다.
# 사용자가 'q'를 입력하면 종료한다.

while True:
    print("""
    계산기
    1: +
    2: -
    3: *
    4: /
    q: 종료
    """)
    operator = input("원하는 계산을 입력하세요: ")
    if operator == 'q':
        break
    a = int(input("정수 1: "))
    b = int(input("정수 2: "))
    def add(a, b):
        result = "%d + %d = %d" % (a, b, a+b) # 포맷 코드 사용(정수형)예제
        with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
            f.write(result)

    def sub(a, b):
        result = f"{a} - {b} = {a-b}" # f-string 사용 예제
        with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
            f.write(result)

    def mul(a, b):
        result = str(a)+" * "+str(b)+" = "+str(a*b)
        with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
            f.write(result)

    def div(a, b):
        result = str(a)+" / "+str(b)+" = "+str(a/b)
        with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
            f.write(result)

    if operator == "1":
        add(a, b)
        print(a,"+",b,"=",a+b)
    elif operator == "2":
        sub(a, b)
        print(a,"-",b,"=",a-b)
    elif operator == "3":
        mul(a, b)
        print(a,"*",b,"=",a*b)
    elif operator == "4":
        div(a, b)
        print(a,"/",b,"=",a/b)
