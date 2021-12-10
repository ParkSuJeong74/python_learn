import sys

# 한수 테스트


def han(x):
    index = 0
    for i in len(x):
        if x[i+1] - x[i] == x[i+2] - x[i-1]:
            index += 1
    if index == len(x) - 1:
        return True


tmp = sys.stdin.readline()
x = list()
for i in str(tmp):
    x.append(i)
print(x[0])

for i in 10000:
    if han(10000) == True:
        print(i)
