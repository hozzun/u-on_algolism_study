# 메모리 31196KB 시간 44ms 코드길이 602
# 백준 2667번 단지번호 붙이기 

def dfs(r, c):
    global danji
    arr[r][c] = 2

    for k in range(4):
        nr = r + di[k]
        nc = c + dj[k]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1: # 1인 부분만 
            danji += 1 # 단지 +1 해줌 
            dfs(nr, nc) # 계속 탐색 

    return danji

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
danji_lst = []
danji = 0 # 단지 1덩어리 안에 몇 개 있는지 세 줄 변수 
cnt = 0 # 단지 몇 덩어리 있는지 세 줄 변수 
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            danji = 1 
            danji_lst.append(dfs(i,j)) # 단지 리스트에 단지 갯수들 추가 
            cnt += 1 # 몇 덩어리 단지 있는지 세줌 

print(cnt)
for danji in danji_lst:
    print(danji)
