# 메모리 31196KB 시간 44ms 코드길이 602
# 백준 2667번 단지번호 붙이기 
def dfs(r,c):
    global danji 

    arr[r][c] = 2

    for k in range(4):
        nr = r + di[k]
        nc = c + dj[k]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
            danji += 1
            dfs(nr, nc)
            
    return danji


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
danji_lst = []
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            danji = 1
            danji_lst.append(dfs(i,j))
            cnt += 1

danji_lst.sort()
print(cnt)
for i in danji_lst:
    print(i)
