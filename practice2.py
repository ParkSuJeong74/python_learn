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
