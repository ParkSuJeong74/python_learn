# 함수

def open_account():
    print("계좌 생성")

# balance : 원금
# 입금


def deposit(balance, money):
    print("입금 완료, 잔액은 {0}원".format(balance+money))
    return balance+money

# 출금


def withdraw(balance, money):
    if balance >= money:
        print("출금 완료, 잔액은 {0}원".format(balance-money))
        return balance-money
    else:
        print("출금 불가능")

# 저녁 출금


def withdraw_night(balance, money):
    commission = 100
    print("출금 완료, 잔액은 {0}원".format(balance-money-commission))
    return commission, balance - money - commission


open_account()
balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)


# 기본값 설정

# 프로필 출력
def profile(name, age, main_lang):
    print("이름 : {0} \t 나이 : {1} \t 주 사용언어 : {2}"
          .format(name, age, main_lang))  # \를 하고 줄바꿈하면 한줄로 인식!


profile("박수정", 25, "python")

# 같은 학교 같은 반 같은 수업일 경우 -> 기본값


def profile_2(name, age=30, main_lang="python"):
    print("이름 : {0} \t 나이 : {1} \t 주 사용언어 : {2}"
          .format(name, age, main_lang))  # \를 하고 줄바꿈하면 한줄로 인식!


profile_2("박수정")
profile_2(main_lang="JAVA", name="박수정")  # 키워드로 호출 가능

# 가변인자


def profile_3(name, age, *language):  # 갯수를 지정하지 않음, list 대신 사용할 수도 있을 듯함!
    print("이름 : {0} \t 나이 : {1}\t"
          .format(name, age), end=" ")
    for i in language:
        print(i, end=" ")
    print()


profile_3("박수정", 25, "Python", "C", "C++", "C#", "Java")

# 지역, 전역 변수
# 군대
gun = 10
# 전역 변수를 함수안에서 사용하는 방법


def checkpoint_1(soldiers):  # 경계근무를 서는 함수
    global gun  # 전역 공간에 있는 gun을 가져옴. global 부재시 새로운 지역변수 만들어짐
    gun -= soldiers  # 경계 근무를 나가면 남은 총이 줄어듬
    print("남은 총 : {0}".format(gun))


print("전체 총 : {0}".format(gun))
checkpoint_1(2)  # 경계근무를 두사람이 나감
print("남은 총 : {0}".format(gun))

gun = 10


def checkpoint_2(gun, soldiers):  # 경계근무를 서는 함수
    gun -= soldiers  # 경계 근무를 나가면 남은 총이 줄어듬
    print("남은 총 : {0}".format(gun))
    return gun  # 변수값을 리턴함


print("전체 총 : {0}".format(gun))
gun = checkpoint_2(gun, 2)  # 리턴값을 받음
print("남은 총 : {0}".format(gun))


# quiz

# 표준 체중을 구하는 프로그램

# (성별에 따른 공식)
# 남 : 키(m) * 키(m) * 22
# 여 : 키(m) * 키(m) * 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#     함수명 : std_weight
#     전달값 : 키(height), 성별(gender)

# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# 출력 : 키 175m 남자의 표준 체중은 67.38kg 입니다.


def std_weight(height, gender):
    if gender == "여자":
        weight = height * height * 21
    else:
        weight = height * height * 22
    print("키 {0}m {1}의 표준 체중은 {2:.2f}kg 입니다."
          .format(height, gender, weight / 10000))


std_weight(165, "여자")
