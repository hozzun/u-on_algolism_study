# 메모리 : 31900
# 시간 : 3868ms

K = int(input())
arr= []

for i in range(K):
    num = int(input())
    if num == 0:   # 입력 받은 수가 0이면 마지막 요소 제거
        arr.pop()
    else:
        arr.append(num)    # 0이 아니라면 append
print(sum(arr))    # 남은 arr 요소의 총합
