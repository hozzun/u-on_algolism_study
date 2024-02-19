# 1) Python(Not sys) - 메모리: 31900KB, 시간: 4044ms
# 2) Python(sys) - 메모리: 31900KB, 시간: 76ms
# 3) PyPy(sys) - 메모리: 114236KB, 시간: 128ms
import sys
input = sys.stdin.readline

K = int(input())

arr = []
for tc in range(K):
    N = int(input())
    if N != 0: # 0이 아니면 arr에 추가
        arr.append(N)
    elif N == 0 and arr != []: # 0이면 최근꺼 제거
        arr.pop()

result = sum(arr) # 더해주고
print(result) # 출력
