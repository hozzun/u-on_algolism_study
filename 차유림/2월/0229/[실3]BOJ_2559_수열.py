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
