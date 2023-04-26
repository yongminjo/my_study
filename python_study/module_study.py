# 모듈 
# 함수, 변수, 클래스를 모아 놓은 파이썬 파일
# 다른 파이썬 프로그램에서 불러와서 사용
# import 명령어로 불러옴

"""
import 모듈 이름
"""

# import my_module
# my_module.add(1, 2) #모듈도 객체이기 때문에 모듈이름.멤버() 형태로 사용
# my_module.sub(1, 2)

"""
from 모듈 이름 import 모듈 함수
from 모듈 이름 import 모듈 함수1, 모듈 함수2
from 모듈 이름 import *  
"""                     # *은 전체라는 의미를 가진다.

# from my_module import add, sub
# add(1, 2)
# sub(1, 2)

# from my_module import *
# add(1, 2)
# sub(1, 2)

# import my_module  # 

from my_calculator import MyCalculator
# my_calculator = MyCalculator() 
# my_calculator.div(10, 0) #Error가 발생시 즉시 중단되기 때문에 고쳐서 에러를
class ZeroCalculator(MyCalculator): # 방지하는 것이 중요하다.
    def div(self, n1, n2):
        if n2 == 0:
            print("0으로 나눌 수 없습니다.")
        else:
            print(f"{n1} / {n2} = {n1 / n2}")

zero_calculator = ZeroCalculator()
zero_calculator.div(10, 0)