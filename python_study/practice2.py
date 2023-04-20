li_1 = ["Hello", "World", "Python"]
# li_1의 원소를 사용하여
# Hello World Python 이라고 출력하세요.

print(li_1[0],li_1[1],li_1[2])
print(li_1[0]+ " " + li_1[1] + " " + li_1[2])
# 조금 더 편한 방법, 
# join(리스트)
# 리스트의 문자열을 합친다.
print(" ".join(li_1))
# 따옴표안에 공백을 넣으면 공백, 문자를 넣으면 문자가 출력.


# li_1의 원소를 사용하여
# HelP라고 출력하세요. 출제자의 의도는 각 값의 글자를 따오는 것.

print(li_1[0][0:3] + li_1[2][0])

li_1.append("HelP")
print(li_1[3])

li_1.remove("HelP")

li_2 = [1, 2, 3]
# li_1과 li_2를 사용하여
# ["Hello", "World", "Python", 1, 2, 3]
# 를 출력하세요.


print(li_1 + li_2)
li_1.extend(li_2)
print(li_1) # .extend 앞에 오는 리스트가 이름이 됨


li_1 = ["Hello", "World", "Python"]
li_2 = [1, 2, 3]

# li_1과 li_2를 사용하여         ★ 못품...ㅜㅜ (insert 함수 이용)
# ["Hello", 1, "World", 2, "Python", 3]
# 를 출력하세요.

li_1.insert(1, li_2[0])
li_1.insert(3, li_2[1])  # 인덱스 주의!(추가되면서 변동됨.)
li_1.insert(5, li_2[2])

print(li_1)



"""
scores = []  #꼭 다시 해보기.
# scores = list() # 위에랑 동일한 기능을 한다.
scores.append(int(input("영어 점수:")))
scores.append(int(input("국어 점수:")))
scores.append(int(input("수학 점수:")))

avg = (scores[0] + scores[1] + scores[2]) / 3
# sum()
# 리스트의 요소를 모두 더한다.
avg = sum(scores) / 3
if avg >= 91:
    print("A")
elif avg >= 81:
    print("B")
elif avg >= 71:
    print("C")
elif avg >= 61:
    print("D")
else:
    print("F")
"""
# 나이와 가지고 있는 돈을 입력받는다
# 가지고 있는 돈으로 물건을
# 몇 개 살 수 있는지와 잔돈을 출력한다.
# 물건의 가격은 500원이다.

# person = list()
# person.append(int(input("나이:")))
# person.append(int(input("소지금:")))

# print(person[1] // 500, "개 살 수 있고,")
# print(int(person[1] % 500), "원이 남아요.")

# 나이와 가지고 있는 돈을 입력받는다
# 가지고 있는 돈으로 물건별로 각각
# 몇 개 살 수 있는지와 잔돈을 출력한다.
# 물건의 가격은 1번 물건 1000원 이다.
# 2번 물건 50원 3번 물건 120원이다.

age = input("나이:")
money = int(input("돈:"))
price = [1000, 50, 120]

print("1번 물건은", money // price[0], "개 살 수 있고")
print(int(money % price[0]), "원이 남아요.")
print("2번 물건은", money // price[1], "개 살 수 있고")
print(int(money % price[1]), "원이 남아요.")
print("3번 물건은", money // price[2], "개 살 수 있고")
print(int(money % price[2]), "원이 남아요.")