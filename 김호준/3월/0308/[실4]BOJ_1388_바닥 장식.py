# Python 메모리: 31120KB, 시간: 40ms, 코드 길이: 676B

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(y, x):
    global graph, visited
    visited[y][x] = True # 방문 처리

    if graph[y][x] == '-':
        # 오른 쪽이랑 같은 것이면 계속 이동
        if x + 1 < M and graph[y][x + 1] == '-' and not visited[y][x + 1]:
            dfs(y, x + 1)
    elif graph[y][x] == '|': # 여기서 개빡침.. 자판기 L에 있는 건줄 알고하다가 답 계속 이상하게 나왔었음..
        # 아래랑 같은 것이면 계속 이동
        if y + 1 < N and graph[y + 1][x] == '|' and not visited[y + 1][x]:
            dfs(y + 1, x)


N, M = map(int, input().split())

graph = [list(map(str, input().rstrip())) for _ in range(N)] # 배열
visited = [[False] * M for _ in range(N)] # 방문

answer = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j)
            answer += 1

print(answer)
