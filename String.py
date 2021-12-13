# String

sentence = '안녕하세요'
sentence_2 = "잘 부탁합니다"
print(sentence)
print(sentence_2)
sentence_3 = '''
이것도
문자열을
나타내는 방법
'''  # 줄바꿈도 포함
print(sentence_3)


# slicing

jumin = "123456-9876543"

print("주민번호 성별 : " + jumin[7])
print("주민번호 연도 : " + jumin[0:2])  # index : 0, 1
print("주민번호 앞자리 : " + jumin[:6])
print("주민번호 뒷자리 : " + jumin[7:])  # 동일
print("주민번호 뒷자리 : " + jumin[-7:])  # 동일


# 문자열 처리 함수

# 소문자로 변경
python = "Python is Amazing"
print(python.lower())

# 대문자로 변경
print(python.upper())

# 대문자인지 확인
print(python[0].isupper())  # True

# 길이
print(len(python))

# 문자 변경
print(python.replace("Python", "Java"))

# "n" 위치 찾기
index = python.index("n")  # 5
print(index)

index = python.index("n", index+1)  # 5 이후로 찾음, 15
print(index)

print(python.find("n"))  # 5
print(python.find("Java"))  # -1
# print(python.index("Java")) # 오류

# 갯수 세기
print(python.count("n"))  # 2
