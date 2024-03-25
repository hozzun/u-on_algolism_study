# BOJ 2178 미로 탐색 [실1]
# PyPy 메모리: 114320KB, 시간: 160ms, 코드 길이: 778B

from collections import deque

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def bfs(y, x, cnt): # bfs
    global answer
    q = deque()
    q.append((y, x, cnt))
    visited[y][x] = True

    while q:
        i, j, count = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if graph[ni][nj] == 1 and not visited[ni][nj]:
                    if ni == N - 1 and nj == M - 1:
                        answer = count + 1 # 맨 끝에 체크해야하므로 + 1
                    visited[ni][nj] = True
                    q.append((ni, nj, count + 1))


N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

answer = 1e9
bfs(0, 0, 1) # (0, 0) 체크해야하므로 1로 시작
print(answer)
