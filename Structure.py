##### list
# 지하철 칸별로 10명, 20명, 30명

subway = [10, 20, 30]
print(subway.index(10))  # 10명이 타고 있는 칸은 몇번째 칸? >> 0번째

# 추가하기
subway.append(50)
print(subway)

# 중간에 추가하기
subway.insert(1, 40)
print(subway) #[10, 40, 20, 30, 50]

# 뒤에서 꺼냄
subway.pop()
print(subway)

# 같은 속성이 몇개인지 확인하기
subway.append(10)
print(subway)
print(subway.count(10))

# 정렬
subway.sort()
print(subway)

# 순서 뒤집기
subway.reverse()
print(subway)

# 속성 모두 지우기
subway.clear()
print(subway)

# 다양한 자료형 같이 가능
arr = ["박수정", 25, True]
subway = [10, 20, 30]
print(arr)

# 병합
arr.extend(subway)
print(arr) # ['박수정', 25, True, 10, 20, 30]


##### Dictionary
# key, value

cabinet = {3:"박수정", 100:"유재석"}

# 같은 출력
print(cabinet[3])
print(cabinet.get(100))

# 다른 점
# print(cabinet[5]) # 오류
print(cabinet.get(5)) # None
print(cabinet.get(5, "사용가능")) # 사용가능 출력

# 값이 있는지 확인하기
print(3 in cabinet) # True
print(5 in cabinet) # False

# key가 문자열 가능
cabinet_2 = {"A-23" : "박수정", "B-97" : "유재석"}
print(cabinet_2["A-23"])

# 새 손님 교체 가능
cabinet_2["B-97"] = "새손님"
print(cabinet_2) # {'A-23': '박수정', 'B-97': '새손님'}

# key나 value만 출력
print(cabinet_2.keys()) # dict_keys(['A-23', 'B-97'])
print(cabinet_2.values()) # dict_values(['박수정', '새손님'])

# key, value 쌍 출력
print(cabinet_2.items()) # dict_items([('A-23', '박수정'), ('B-97', '새손님')])

# 손님 지우기
del cabinet_2["B-97"]
print(cabinet_2) # {'A-23': '박수정'}

# 폐점
cabinet_2.clear()
print(cabinet_2)


##### Tuple
# 고정된 값을 가짐
# add 불가능

menu = ("돈까스", "생선까스")
print(menu[0])

(name, age, hobby) = ("사람", 25, "코딩")
print(name, age, hobby) # 변수 한번에 선언 가능!


##### 집합(set)
# 중복 불가능, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}

# list -> set
python = set(["사람1", "사람2"])
java = {"사람1", "사람5", "사람6"}

# set 교집합
print(java & python) # {'사람1'}
print(java.intersection(python)) # {'사람1'}

# set 합집합
print(java | python) # {'사람2', '사람6', '사람1', '사람5'}
print(java.union(python)) # {'사람2', '사람6', '사람1', '사람5'}

# set 차집합
print(java - python) # {'사람6', '사람5'}
print(java.difference(python)) # {'사람6', '사람5'}

# set에 추가하기
python.add("사람9")
print(python)

# set에서 삭제하기
python.remove("사람2")
print(python)


##### 자료구조 변경하기
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # {'우유', '주스', '커피'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # ['커피', '우유', '주스'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # ('커피', '우유', '주스') <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) # {'우유', '주스', '커피'} <class 'set'>


##### suffle, sample
from random import *
lst = [1, 2, 3, 4, 5]
shuffle(lst) # 무작위로 순서 바꿈
print(lst)
print(sample(lst, 1)) # 1개를 뽑음


##### quiz
'''
댓글 작성자 중에 추첨을 통해 1명 치킨, 3명은 커피 쿠폰

조건1 : 댓글은 20명 작성, 아이디는 1~20
조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복은 불가능
조건3 : random 모듈의 shuffle과 sample 활용

출력 :
 -- 당첨자 발표 --
 치킨 당첨자 : 1
 커피 당첨자 : [2, 3, 4]
 -- 축하합니다 --
'''

from random import *
# 1부터 20까지 숫자 list
comment = range(1, 20)
comment = list(comment)

shuffle(comment)
print(comment)

check = sample(comment, 4)
print(check)

print(" -- 당첨자 발표 --")
print(" 치킨 당첨자 : {0}".format(check[0]))
print(" 커피 당첨자 : {0}".format(check[1:]))
print(" -- 축하합니다 --")