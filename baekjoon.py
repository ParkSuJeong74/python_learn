import sys

c = int(sys.stdin.readline())

for j in range(c):
    score = list(map(int, sys.stdin.readline().split()))
    sum = 0
    well = 0
    for i in range(1, score[0]+1):
        sum += score[i]
    avg = sum / score[0]
    for i in range(1, score[0]+1):
        if score[i] > avg:
            well += 1
    print("{0:.3f}%".format(well / score[0] * 100))
    del score[0:(score[0]+1)]