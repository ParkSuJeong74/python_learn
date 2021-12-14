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


# 문자열 포맷
# %
print("나는 %d살입니다." % 20)  # s로도 가능
print("나는 %s를 좋아합니다." % "파이썬")
print("Apple %c로 시작합니다." % "A")  # s로도 가능

# 두 개
print("나는 %s과 %s를 좋아합니다." % ("파이썬", "Java"))

# format index
print("나는 {0}과 {1}를 좋아합니다.".format("파이썬", "Java"))
print("나는 {1}과 {0}를 좋아합니다.".format("파이썬", "Java"))  # 반대

# format 변수
print("나는 {age}살이고 {lang}를 좋아합니다.".format(age=20, lang="Java"))

age = 25
lang = "파이썬"
print(f"나는 {age}살이고 {lang}를 좋아합니다.")


# 탈출문자
# \n : 개행

print("안녕하세요\n잘부탁합니다")
print("저는 \"사람\"입니다")  # 저는 "사람"입니다

# \\ == \
print("C:\\Users\\dell\\vscode-workspace\\python_learn")  # C:\Users\Drimsys\vscode-workspace\python_learn

# \r : 커서를 맨 앞으로
print("Red Apple\rPine")  # PineApple

# \b : 백스페이스 (한글자 삭제)
print("Redd\b Apple")  # Red Apple

# \t : tab
print("Red\tApple")  # Red     Apple


# quiz
'''
사이트별로 비밀번호를 만들어주는 프로그램
http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

출력:
생성된 비밀번호 : nav51!

'''

url = "http://naver.com"
my_url = url.replace("http://", "")
my_url = my_url[:my_url.index('.')]
password = my_url[:3]+str(len(my_url))+str(my_url.count('e'))+"!"

print("생성된 비밀번호 : {0}".format(password))
