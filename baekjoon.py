import sys

# 함수


def d(n):
    sum = 0
    for i in range(n):
        sum += int(n) // (10*(i+1))
    sum += int(n) % 10
    return sum


arr = list()
for i in range(10000):
    arr.append(i)
    for j in range(10000):
        if d(i) == arr[j]:
            arr.remove(d(i))
    print(arr[i])
