# ㅈㅅㅈㅅ 다시 못풀어봄..
# 시간 초과

from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

arr = deque()
for _ in range(N):
    h = int(input())
    arr.append(h)

answer = 0
while True:
    if len(arr) == 1:
        # answer += count
        break

    count = 0

    check = arr.popleft()
    for i in range(len(arr)):
        if check > arr[i]:
            count += 1
            if i == len(arr) - 1:
                answer += count
                break

        elif check <= arr[i]:
            answer += count
            break

print(answer)
