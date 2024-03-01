# 2번 실패 후 성공 !!!!  
백준 실버3 2559번 수열 메모리 123228kb 시간 3716ms 에반데? ㅋㅋㅋㅋㅋㅋㅋㅋ
# 아영언니가 1 2 3 4 5 이면 1 2 3 하고 1 뺴고 4 추가해서 했다 라는 말을 듣고 다시 해봤음 
N, K = map(int, input().split())
arr = list(map(int, input().split()))
max_v = - 99999
sum_v = 0
sum_lst = []
for i in range(N):
    sum_lst.append(arr[i])
    if len(sum_lst) == K:
        sum_v = sum(sum_lst)
        if max_v < sum_v:
            max_v = sum_v
        sum_lst.pop(0)

print(max_v)


# 백준 실버3 2559번 수열  시간초과난다잉 ㅠ ㅠ
N, K = map(int, input().split())
arr = list(map(int, input().split()))
max_v = - 99999
for i in range(N - K + 1):
    sum_v = 0
    for j in range(i, i + K):
        sum_v += arr[j]
    if max_v < sum_v:
        max_v = sum_v

print(max_v)

# 슬라이싱하고 sys해도 안되네... ㅠ 
import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
max_v = - 99999

for i in range(N - K + 1):
    sum_v = 0
    sum_v = sum(arr[i:i+K])
    if max_v < sum_v:
        max_v = sum_v

print(max_v)
