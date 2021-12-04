##### 예외처리
print("Hello")

try:
    n1 = int(input("숫자"))
    n2 = int(input("숫자"))
    print("{0} / {1} = {2}".format(n1, n2, int(n1/n2)))
except ValueError:
    print("에러!")
except ZeroDivisionError as err:
    print(err)