#  dictionary(딕셔너리) 자료형
# key-value 형태
# key: value (이런 형식으로 작성)
person = {
    "이름": "이름",
    "나이": 18,
    "점수": 
        {"영어": 80,
         "국어": 90,
         "수학": 100
    }, 
    1: "ㅎㅎ"
}
print(person["나이"])   # 인덱스 말고 키값으로 접근
print(person["점수"]["영어"]) 

# dict_1 = {1: 'a'}
# dict_1['b'] = 2   # 'b': 2 - key_value 쌍 추가
# dict_1[1] = 'c'  # 1의 value값을 수정
# del dict_1[1]   # key-value 쌍 삭제
# print(dict_1)

dict_2 = {1:'a', 2:'b', 3:'c'}
# keys()
# 딕셔너리에서 key값만 리스트 형태로 돌려준다.
dict_keys = dict_2.keys()
print(dict_keys)
# values()
# 딕셔너리에서 value값만 리스트 형태로 돌려준다.
dict_values = dict_2.values()
print(dict_values)
# items()
# 딕셔너리에서 key-value 쌍을 튜플로 묶은 값을 리스트 형태로 돌려준다.
dict_items = dict_2.items()
print(dict_items)

# get(key)
# key에 대응되는 value를 돌려준다.
# key값이 존재하지 않으면 None을 돌려준다.
print(dict_2.get("나이", "나이 불명"))
# 키값이 있으면 그에 상응하는 값을 불러와 주고, 
# 지금처럼 상응하는 결과가 없으면 '나이 불명'을 출력한다.

# clear()
# 딕셔너리 안의 모든 요소를 삭제한다,
dict_2.clear()
print(dict_2)