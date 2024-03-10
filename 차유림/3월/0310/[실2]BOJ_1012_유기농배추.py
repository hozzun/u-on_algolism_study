def dfs(r,c):
    baechu[r][c] = 2
    for k in range(4):
        nr = r + di[k]
        nc = c + dj[k]
        if 0 <= nr < M and 0 <= nc < N and baechu[nr][nc] == 1:
            dfs(nr,nc)


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    baechu = [[0] * M for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    cnt = 0
    for _ in range(K):
        y, x = map(int, input().split())        
        baechu[x][y] = 1
        
    
    for j in range(M):
        for i in range(N):
            if baechu[i][j] == 1:
                dfs(i, j)
                cnt += 1
    
    print(cnt)
