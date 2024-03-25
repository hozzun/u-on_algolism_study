import sys
sys.setrecursionlimit(10**6)
M, N, K = map(int, input().split())
area = [[0] * N for _ in range(M)]
for _ in range(K):
    r1, c1, r2, c2 = map(int, input().split())
    for r in range(c1, c2):
        for c in range(r1, r2):
            area[r][c] = 1

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

real_area = 0
cnt_lst = []
cnt = 0

def dfs(r, c):
    global real_area
    area[r][c] = 2

    for k in range(4):
        nr = r + di[k]
        nc = c + dj[k]
        if 0 <= nr < M and 0 <= nc < N and area[nr][nc] == 0:
            real_area += 1
            dfs(nr, nc)
    return real_area

for i in range(M):
    for j in range(N):
        if area[i][j] == 0:
            real_area = 1
            # dfs(i, j)
            cnt_lst.append(dfs(i, j))
            cnt += 1

print(cnt)
cnt_lst.sort()
print(*cnt_lst)
        
