##### if

# 비, 눈 => 우산
# 미세먼지 => 마스크
# 나머지 => 챙길 거 없음

weather = input("오늘 날씨는? ")
if weather == '비' or weather == '눈':
    print("우산 챙겨요")
elif weather == "미세먼지":
    print("마스크 챙겨요")
else:
    print("챙길 것 없습니다")


# 30 이상 : 너무 더움
# 10~30 : 괜찮음
# 0~10 : 외투 필요
# 0 이하 : 추움!

temp = int(input("기온은 어때요?")) # int 형으로 입력받음
if 30 <= temp:
    print("너무 더워요")
elif 10 <= temp and temp <30:
    print("괜찮아요")
elif 0 <= temp and temp <10:
    print("외투 챙기기")
else:
    print("너무 추워요!")


##### for
# 대기번호 : 0~4

for waiting in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting))

# 대기번호 : 0~99

for waiting in range(100):
    print("대기번호 : {0}".format(waiting))


# 대기번호 : 5~10

for waiting in range(5, 11):
    print("대기번호 : {0}".format(waiting))

# 스타벅스에 손님 부르기

starbucks = ["first", "second", "third"]
for customer in starbucks:
    print("{0}, 커피가 준비됨".format(customer))


##### while
# 다섯번 부르면 커피 버림

customer = "first"
i = 5

while i >= 1: # true : 무한루프
    print("{0}, 커피가 준비됨. {1}번 남았습니다.".format(customer, i))
    i-=1
    if i == 0:
        print("커피 폐기")

# 손님 부름
customer = "second"
person = "unknown"

while person != "second": # true : 무한루프
    print("{0}, 커피가 준비됨.".format(customer))
    person = input("이름? ")

