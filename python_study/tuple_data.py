# tuple(튜플)형
# 튜플은 element의 값을 수정할 수 없다.
# mutable / immutable
# mutable 수정 가능한 ex) list형, dictionary형
# immutable 수정 불가능 ex) int, float, str, tuple

# my_list = [1, 2, 3]
# my_list[0] = 5
# print(my_list)
 
# my_tuple = (1, 2, 3)
# my_tuple[0] = 5 # Error => 튜플형은 수정 불가능
# # print(my_tuple)

# tuple_1 = ("Hello", "World", "Python")
# t2 = (1, 2, 3, 4, 5)
# t3 = (1, 2, "Hello")
# t4 = 1, 2, 3  # 괄호 없이 만들 수 있지만, 가독성을 위해 괄호를 사용하는 걸 권장
# t5 = (1, 2, (3, 4, 5)) # 괄호 안에 괄호를 사용해서 만들 수 있다.

# # 안에 내용을 삭제할 수도 없다.

# t6 = tuple_1 + t2
# t7 = t3 * 3
# t7 = t3 * 4

# print(t7)

# print(t3[0:2])
# print(len(t3))

# print(t5[2][1])

# 값을 삭제, 추가, 정렬(순서를 뒤집는다던지) 안됨!!
#  append, sort 등등... 괄호 안에가 변경되는건 X
# 리스트와 동일한 점이 많음. 꼭 구분하기 바람...!! 
# t8 = (5, 3, 1, 4, 2)

# for i in t8:
#     print(i)
# 리스트형태와 동일하게 인덱스를 그대로 따라와서 표출..
# 순서와 값이 중요한 형태의 데이터! 