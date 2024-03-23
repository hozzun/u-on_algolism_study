# 파이썬     34096 KB,   80 ms, 883 B
# 파이파이  114060 KB,  168 ms


from collections import deque

def bfs(a, b):
    Q = deque()
    Q.append((a, b))
    res = 1               # 현재 구역 넓이
    square[a][b] = 1      # 방문 처리
    
    while Q:
        x, y = Q.popleft()
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < M and 0 <= nj < N and square[ni][nj] == 0:
                square[ni][nj] = 1    # 방문처리
                Q.append((ni, nj))
                res += 1

    return res     # 넓이 return

M, N, K = map(int, input().split())   # 세로, 가로, 사각형 수
square = [[0] * N for _ in range(M)]
area = []   # 구역 넓이
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    # 사각형 채우기
    for i in range(y1, y2):
        for j in range(x1, x2):
            square[i][j] = 1

# 빈구역 찾기
for r in range(M):
    for c in range(N):
        if square[r][c] == 0:
            area.append(bfs(r, c))    # 현재 구역 area에 append

print(len(area))   # 구역 수
area.sort()        # 정렬
print(*area)       # 구역 넓이
