# 예외처리

try:
    print("나누기 계산기")
    nums = []  # list()와 동일
    nums.append(int(input("숫자 : ")))
    nums.append(int(input("숫자 : ")))
    # nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# 입력 값이 int 형이 아님
except ValueError:
    print("에러!")
# 0으로 나눌 수 없음
except ZeroDivisionError as err:
    print(err)
# list index
except Exception as err:
    print("알 수 없는 오류 발생! 내용 : {0}".format(err))
