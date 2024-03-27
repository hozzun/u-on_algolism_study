# Python 메모리: 39720KB, 시간: 632ms, 코드 길이: 997B

from collections import deque
di = [1, 0, -1, 0] # 상하좌우
dj = [0, 1, 0, -1]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = 0

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                # 0 은 0 처리
                if graph[ni][nj] == 0 and visited[ni][nj] == -1:
                    visited[ni][nj] = 0
                # 1은 1씩 증가
                elif graph[ni][nj] == 1 and visited[ni][nj] == -1:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)] # 기본 값 -1 로

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

# 원래 그래프에서 0 인데, bfs로 못도는 곳 0 처리 해주기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0: # 그래프 0 이면 0 출력
            print(0, end=' ')
        else: # 아니면 visited 저장 값들 출력
            print(visited[i][j], end=' ')
    print()


# 확인용
# for i in range(N):
#     print(*visited[i])
#
# print('-------------')
#
# for i in range(N):
#     print(*graph[i])
