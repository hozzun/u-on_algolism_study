# 1388번 바닥장식 메모리 31120kb 시간 44ms 코드길이 596
def dfs_garo(r,c): # - 탐색
    if arr[r][c] == '-': # 바닥장식이 - 라면 
        arr[r][c] = 1 # 1로 바꿔준다

        if c + 1 < M and arr[r][c+1]: # 열위치 + 1 < M 이고 오른쪽칸 - 이면 
            dfs_garo(r, c + 1) # 탐색 계속 고고

def dfs_saero(r,c): # | 탐색
    if arr[r][c] == '|':
        arr[r][c] = 1

        if r + 1 < N and arr[r+1][c]: # 행위치 + 1 < N 이고 밑에 칸이 | 이면 
            dfs_saero(r+1, c) # dfs 고고


N, M = map(int, input().split())
arr = [] # arr에 리스트로 인풋해서 추가해줌 
for _ in range(N):
    arr.append(list(input()))

cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '-': # 바닥장식이 - 이면
            dfs_garo(i, j) # 가로 수행
            cnt+= 1
        elif arr[i][j] == '|':
            dfs_saero(i,j)
            cnt += 1

print(cnt)


