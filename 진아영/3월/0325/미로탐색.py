from collections import deque

N, M = map(int, input().split())    # 도착점 N번째줄, M번째 칸
maze = [list(input()) for _ in range(N)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def escape(i, j):
    Q = deque()
    Q.append((i, j))
    maze[i][j] = 1

    while Q:
        r, c = Q.popleft()
        if r == N-1 and c == M-1:
            return maze[r][c]

        for k in range(4):
            ni = r + di[k]
            nj = c + dj[k]
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == '1':
                Q.append((ni, nj))
                maze[ni][nj] = maze[r][c] + 1


print(escape(0, 0))
