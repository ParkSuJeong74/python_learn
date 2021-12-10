# if

# 비, 눈 => 우산
# 미세먼지 => 마스크
# 나머지 => 챙길 거 없음

from random import *  # 마지막 난수 생성 quiz에 사용


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

temp = int(input("기온은 어때요?"))  # int 형으로 입력받음
if 30 <= temp:
    print("너무 더워요")
elif 10 <= temp and temp < 30:
    print("괜찮아요")
elif 0 <= temp and temp < 10:
    print("외투 챙기기")
else:
    print("너무 추워요!")


# for
# 대기번호 : 0~4

for waiting in [0, 1, 2, 3, 4]:
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


# while
# 다섯번 부르면 커피 버림

customer = "first"
i = 5

while i >= 1:  # true : 무한루프
    print("{0}, 커피가 준비됨. {1}번 남았습니다.".format(customer, i))
    i -= 1
    if i == 0:
        print("커피 폐기")

# 손님 부름
customer = "second"
person = "unknown"

while person != "second":  # true : 무한루프
    print("{0}, 커피가 준비됨.".format(customer))
    person = input("이름? ")

# continue, break
# 책을 읽어야하는 학생들 중 결석생이 있을 때
absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue  # 다음 반복으로 넘어감
    elif student in no_book:
        print("수업 끝. {0}는 교무실".format(student))
        break  # 반복 끝
    print("{0}, 책 읽어".format(student))

# 한줄 for
# 출석번호 앞에 100 붙이기

students = [1, 2, 3, 4, 5]
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students_2 = ["박수정", "Icon Man"]
students_2 = [len(i) for i in students_2]
print(students_2)

# 학생 이름을 대문자로 변환
students_3 = ["Icon Man", "Thor", "I am groot"]
students_3 = [i.upper() for i in students_3]
print(students_3)


# quiz

# Cocoa 서비스를 이용하는 택시 기사이다.
# 50명의 승객과 매칭 기획가 있을 때, 총 탑승 승객 수 구하기

# 조건1  : 승객별 운행 소요 시간은 5~50분 사이의 난수

# 조건2 : 당신은 소요 시간 5~15분 사이의 승객만 매칭

# 출력 :
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [0] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 분

count = 0
for i in range(50):
    lack_time = randint(1, 50)
    if lack_time >= 5 and lack_time <= 15:
        bool = "0"
        count += 1
    else:
        bool = " "
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(bool, i, lack_time))
print("총 탑승 승객 : {0} 분".format(count))
