# 런타임에러 10억짜리 안나옴 다른건 다나옴 (시간 계산 안함 ㅋㅋ)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def f(x):
    global cnt
    if x >= V:
        cnt += 1
        print(cnt)
        return
    elif x < V:
        if x == 0:
            x + A
        else:
            cnt += 1
            x -= B
            pass
    f(x + A)

A, B, V = map(int, input().split())
cnt = 0
f(0)
