# 시간초과
# dp 공부해서 도전해볼 예정

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def recur(k, s):
    global answer
    if k > T:
        return

    if k <= T:
        answer = max(s, answer)

    for i in arr:
        if not visited[i[1]]:
            visited[i[1]] = True
            recur(k + i[0], s + i[1])
            visited[i[1]] = False


N, T = map(int, input().split())
arr = []
for _ in range(N):
    K, S = map(int, input().split())
    arr.append((K, S))

visited = [False] * 10001
answer = 0
recur(0, 0)
print(answer)
