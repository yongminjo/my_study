# 객체지향(oop, object oriented programming) -----> 파이썬
# 객체와 객체 사이의 상호작용으로 프로그램을 구성하는 프로그래밍 패러다임

# 객체지향의 특징
# 추상화 : 공통된 속성이나 기능 도출 *
# 캡슐화 : 데이터의 구조와 연산을 결합 *
# 상속 : 상위 개념의 특징이 하위 개념에 전달
# 다형성 : 유사 객체의 사용성을 그대로 유지

# 객체는 추상화와 캡슐화의 결과
# 객체는 데이터 필드와 메소드를 가진다.

# 클래스는 객체를 정의한 것(객체의 설계도)
# 데이터 필드(멤버 변수, 속성)
# 객체가 가지고 있는 변수
# 메소드
# 객체가 가지고 있는 함수 
"""
class 클래스이름 :
    클래스 멤버 변수
    메소드
"""
# 클래스 이름도 변수 이름 규칙 지켜야 함.
# 클래스 이름 컨벤션(관용)
# 첫 글자 대문자
# 언더바(_) 안쓰기
# 단어 구분될 때 대문자
# class Car:    # Car class 안에서 함수가 정의된 것이기 때문에 그 안에서만 호출 할 수 있다.
#     def move(self):    # 클래스 내부의 함수 ; 메소드
#         print("move")

# class SportsCar:
#     pass

# 인스턴스
# 클래스를 통해 생성된 객체
# my_car = Car() 
# my_car.move()
# . --> 객체 멤버 접근 연산자(객체가 가지고있는 멤버에 접근 혹은 호출.)

# li = [1,2,3,4,5]
# li.append(6)
# 파이썬에서는 모든게 객체다.

# 내장함수 type()
# 데이터의 자료형을 반환한다
# print(type(li))
# n = 10
# print(type(n))
# print(type("Hello"))

# str(문자열) 메소드
# upper()
# 모두 대문자로 변경
# s = "Hello"
# print(s.upper())

# lower()
# s = "Hello"
# print(s.lower())

# strip()
# 문자열 양쪽 끝의 특정 문자를 제거 (보통은 공백 제거)
# s1 = "          Hello           "
# print(s1.strip())
# lstrip(), rstrip()
# 왼쪽, 오른쪽 끝의 특정 문자를 제거
# print(s1.lstrip())
# print(s1.rstrip())
# split()
# 구분자로 분할하여 리스트로 반환
# s2 = "Hello,world,Python"
# print(s2.split(','))
# replace()
# 문자열의 특정 부분을 대체
# print(s2.replace(',',' '))
# s2 = s2.replace(',', ' ') # 재할당. 수정이 아님.
# print(s2)

# "Hello" -> "hello" # 재할당 하는 방법. 절대 수정 아님.
# s3 = "Hello"
# s3.lower()
# s4 = s3.replace("H", "h")
# print(s4)

# self 매개변수(parameter)
# 모든 메소드의 첫번째 매개변수
# 메소드의 정의에는 사용되지만, 호출에는 사용되지 않음
# 객체 자신을 참조하여 클래스에 정의된 멤버에 접근할 때 사용
# class Person:
#     def say(self):
#         self.name = "사람1"
#         print("Hello :-)")

#     def move(self):
#         pass

#     def eat(self, food):
#         self.sleep()
#         print(f"{self.name}이 {food}을/를 먹었습니다.")

#     def sleep(self):
#         print(f"{self.name}이 잠을 잤습니다.")

# person1 = Person()
# person1.say()
# person1.eat("밥")

# initializer (이니셜라이저 / 초기화? 초기자?) 
# initialize 초기화/만든다 라고 봐야할듯.
# refresh 아님주의!! 

# class Person:
#     def __init__(self, name, age, gender, phone):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.phone = phone
#         print("initialize")

#     def say_name(self):
#         print(self.name)

#     def introduce(self):
#         print(f"안녕하세요. 저는 {self.name}입니다.")
#         print(f"나이는 {self.age}살이고, {self.gender}입니다.")

# print("before")
# person2 = Person("이름", 20, "남자", "010-1234-5678") # 객체가 만들어질 때 이니셜라이즈가 됨
# print("after")
# person2.say_name()

# Person 클래스에 introduce 메소드를 추가
# 이름, 나이, 성별을 print하는 메소드
# person2.introduce()


# 상속 inheritance
# class Animal:
#     def __init__(self,name):
#         self.name = name  #name을 입력받고 멤버 변수로 저장하지만, 둘은 다른 객체임!!
#         print(f"{self.name}가 생성되었습니다.")

#     def say(self):
#         print("")

# class Dog(Animal):  # 괄호 안에 상속받을 클래스를 입력하면 상속.
#     def say(self):  # 메소드 재정의(method overriding(덮어쓰기))
#         print("멍멍")

# my_dog = Dog("백구")
# my_dog.say()

# class Cat(Animal):
#     def say(self):
#         print("야옹")

# my_cat = Cat("나비")
# my_cat.say()

class Student: #이름, 나이, 학교, 학년을 멤버 변수로 저장하는 메소드를 정의하세요.
    def __init__(self, name, age, school, grade):
        self.name = name
        self.age = age
        self.school = school
        self.grade = grade
        
    def introduce(self): #이름, 나이, 학교, 학년을 print하는 메소드를 정의하세요.
        print(f"안녕하세요. 저는 {self.name}이고, {self.age}살 입니다.")
        print(f"{self.school}에 다니고, {self.grade}학년입니다.")

stu1 = Student("홍길동", 20, "서울대학교", 1)
stu2 = Student("손흥민", 21, "서울대학교", 2)
stu3 = Student("류현진", 22, "서울대학교", 3)
stu_list = [stu1, stu2, stu3]
for stu in stu_list:
    stu.introduce()
