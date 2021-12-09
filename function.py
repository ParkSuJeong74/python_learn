##### 함수

def open_account():
    print("계좌 생성")

#balance : 원금    
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
#balance = withdraw(balance, 2000)
#balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)


##### 기본값 설정