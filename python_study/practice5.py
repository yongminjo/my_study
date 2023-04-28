# 거꾸로 배열해도 같은 단어 또는 문장이 되는 
# 회문(palindrome)인지 판별하는 함수를 정의하세요.
# 함수에 문자열을 입력받고 회문이면 True 또는 False를 반환하도록 정의하세요.

# 함수이름 : is_palindrome
# 반환 값 : True or False

# def is_palindrome(input_string):
#     input_string = input_string.replace(" ", "")
#     length = len(input_string)
#     for i in range(length//2):  # range는 무조건 정수형 값이 들어가야함..!
#         if input_string[i] != input_string[length -1 -i]:
#             return False
#     return True

# def is_palindrome(input_string):                 # 대오타시대.... 오타 잘 확인 할 것.!!!
#     input_string = input_string.replace(" ", "") # 문자열 중간에 공백 제거 why,
#     return input_string == input_string[::-1]    #  "다시V합창합시다", "소주V만병만V주소" 둘 다 회문이지만
#                                                  #  띄어쓰기 횟수가 다르기 때문에 회문이 아닌것처럼 걸러짐.
# result = is_palindrome("다시 합창합시다")
# print(result)

