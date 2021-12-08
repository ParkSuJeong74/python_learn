print("hello world!"*5)
print(not(5 > 10))  # True
print(not True)  # False

# 애완동물을 소개해주세요
'''
변수 선언과 str() 사용
여러문장 주석이 됩니다.
'''
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = (age >= 3)

print("우리집 " + animal + "의 이름은 " + name + " 입니다")
# print(name+"는 "+str(age)+"살이며, 취미는 "+hobby+"입니다")
print(name+"는 ", age, "살이며, 취미는 ", hobby, "입니다")
print(name+"는 어른일까요? "+str(is_adult))


'''
quiz) 변수를 이용해 다음 문장 출력
변수명 : station
변수값 : "사당", "신도림", "인천공항" 순서대로 입력
출력문장 : xx 행 열차가 들어오고 있습니다.
'''
station = "사당"
print(station+" 행 열차가 들어오고 있습니다.")
station = "신도림"
print(station+" 행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station+" 행 열차가 들어오고 있습니다.")

# 연산

print(7/3)  # 2.3333333333333335
print(7//3)  # 2 : 몫만
print(5**2)  # 25

print(3 == 3)  # True
print(3 != 3)  # False
print(not(3 != 3))  # True
print(not(3 != 3) and (3 > 2))  # True : 둘다 True
print(not(3 != 3) & (3 < 2))  # False : 하나가 False

print(not(3 != 3) or (3 > 2))  # True : 둘다 True
print(not(3 != 3) | (3 < 2))  # True : 하나가 True

print(5 > 4 > 3)  # True
print(6 > 4 > 5)  # False

num = 2 + 3 * 4  # 14
print(num)
num = num+2  # 16
print(num)
num += 2  # 18
print(num)

num %= 5  # 3
print(num)

########

# list

# 지하철 칸별로 10명, 20명, 30명

subway = [10, 20, 30]
print(subway.index(10))  # 10명이 타고 있는 칸은 몇번째 칸? >> 0번째
subway.append(50)
