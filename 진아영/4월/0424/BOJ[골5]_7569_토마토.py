# 가로세로높이 범위 조건 N, M, H로 줘서 다른 차원으로 침범하지 않게 왔다갔다 잘 작동되는데 21%에서 틀림...
# 그래서 3차원으로 풀었음

# 파이파이 216412 KB, 700 ms
# 파이썬  48592 KB, 4324 ms


from collections import deque

M, N, H = map(int, input().split())  # 가로, 세로, 높이
tomatos = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
di = [-1, 1, 0, 0, 0, 0]
dj = [0, 0, -1, 1, 0, 0]
dk = [0, 0, 0, 0, -1, 1]  # 간단하게 위아래 차원 만큼만 추가해서 기본 bfs랑 똑같이 풀었음

Q = deque()

for a in range(H):
    for b in range(N):
        for c in range(M):
            if tomatos[a][b][c] == 1:
                Q.append((a, b, c))

while Q:
    ca, cb, cc = Q.popleft()

    for n in range(6):
        na = ca + di[n]
        nb = cb + dj[n]
        nc = cc + dk[n]
        if 0 <= na < H and 0 <= nb < N and 0 <= nc < M and not tomatos[na][nb][nc]:
            tomatos[na][nb][nc] = tomatos[ca][cb][cc] + 1
            Q.append((na, nb, nc))

day = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatos[i][j][k] == 0:
                print(-1)
                exit(0)
            day = max(day, tomatos[i][j][k])

print(day-1)



#------------------------2차원으로 푼 실패 코드------------------------------------------------------



from collections import deque

M, N, H = map(int, input().split())  # 가로, 세로, 높이
tomatos = [list(map(int, input().split())) for _ in range(N * H)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


Q = deque()

for a in range(N * H):
    for b in range(M):
        if tomatos[a][b] == 1:
            a, c = a % N, a // N
            Q.append((a, b, c))

while Q:
    i, j, h = Q.popleft()

    # 옆 토마토 판단
    for n in range(4):
        ni = i + di[n]
        nj = j + dj[n]
        if 0 <= ni < N and 0 <= nj < M and not tomatos[ni + N * h][nj]:
            tomatos[ni + N * h][nj] = tomatos[i + N * h][j] + 1
            Q.append((ni, nj, h))

    # 위아래 토마토 판단
    for n in [-1, 1]:
        nh = h + n
        if 0 <= nh < H and not tomatos[i + N * nh][j]:
            tomatos[i + N * nh][j] = tomatos[i + N * h][j] + 1
            Q.append((i, j, nh))

day = 0

for r in range(N * H):
    for c in range(M):
        if tomatos[r][c] == 0:
            print(-1)
            exit(0)
        day = max(day, tomatos[r][c])

print(day-1)
