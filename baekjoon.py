# 셀프 넘버를 출력하기
# 생성자가 없으면 셀프 넘버
# d(75) = 75+7+5 = 87 : 87는 75의 생성자

def d(n):
    sum = 0
    for i in range(len(str(n))):
        sum += n // (10 * (i+1))
    sum += n % 10  # n은 sum의 생성자
    sum += n
    return sum


arr = list(range(1, 20))
arr_remove = list()
for i in range(20):
    for j in range(i):
        if arr[i] == d(j+1):
            arr_remove.append(i)
    arr = arr - arr_remove
    print(arr[i])
