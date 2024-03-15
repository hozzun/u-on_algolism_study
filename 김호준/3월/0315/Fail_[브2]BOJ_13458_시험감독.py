# 시간 초과
# 반복문 2개쓰면 안된다는 것을 알지만.. 2개 안쓰고 어케품!! 생각이 안나~
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = 0
for i in arr:
    i = i - b
    cnt += 1

    if i > 0:
        while i > 0:
            i = i - c
            cnt += 1

print(cnt)
