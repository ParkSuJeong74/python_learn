# n 이하 한수의 개수 출력
import sys
# 한수 판별 함수
def han_number(num): # num가 한수인지 아닌지
    arr = list(map(int, str(num)))
    same_div = set([])
    
    for i in range(len(arr) -1):
        div = arr[i] - arr[i+1]
        same_div.add(div)
        
    same_div_list = list(same_div)
    if len(same_div_list) == 1:
        return True
    else:
        return False


num = int(sys.stdin.readline())
count = 0

for i in range(1, (num+1)):
    if len(str(i)) < 3:
        count+=1
    elif len(str(i)) >= 3 and han_number(i) == True:
        count+=1
print(count)