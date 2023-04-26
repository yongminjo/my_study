# 예외 처리
# 오류 발생을 잡아내서 처리하는 것

# li = [1, 2, 3, 4, 5]
# li[100] # index error

# 100 / 0 # zero division error

# f = open("없는파일", "r") # file not found error

# 에러 발생 시 프로그램 중단하고 에러 메시지를 보여준다.

# 에러 처리 구문
# try ~ except
# try 블록에는 오류가 발생할 수 있는 코드
# except 블록에는 오류가 발생했을 때 수행할 코드
# 오류가 발생하지 않으면 except 블록의 코드는 실행되지 않는다.

# try:
#     100 / 0
# except Exception as e:  # Exception은 오류 객체.
#     print(e)


# try:
#     [1, 2, 3, 4, 5][100]
# except ZeroDivisionError as e: # 구체적으로 특정 에러를 잡아내서 사용할 수 있다.
#     print(e, "0으로 나눌 수 없습니다.")
# except IndexError as e:
#     print(e, "인덱싱할 수 없습니다.")

# print("에러 발생 후")

# finally 
# 예외 발생 여부와 상관 없이 항상 마지막에 수행되는 코드

# try:
#     f = open("없는파일", "r")
# except:
#     print("에러 발생")
# finally:
#     f.close()

# else
# 오류가 발생하지 않으면 실행되는 코드

# try:
#     age = int(input("나이: "))
# except:
#     print("입력이 잘못 되었습니다.")
#     print("숫자를 입력해주세요.")
# else:
#     if age >= 20:
#         print("성인입니다.")
#     else:
#         print("미성년자입니다.")


# 일부로 에러를 발생시켜야 할 때 (완벽히 기능을 구현하지 않았거나 하는 이유 등)
class Bird: 
    def fly(self):
        raise NotImplementedError # raise 뒤에는 에러의 객체가 따라와야한다.
    
my_bird = Bird()
my_bird.fly()
