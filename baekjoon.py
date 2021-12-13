import sys

t = int(sys.stdin.readline())

for i in range(t):
    s = list(map(str, sys.stdin.readline()))
    result = ""
    for j in s[2:-1]:
        result += j*(int(s[0]))
    print(result)
