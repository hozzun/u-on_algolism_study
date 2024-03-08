# 4963번 섬의 개수 
# swea 스택2 미로 확인용 문제를 참고함 
# 리커젼 에러 나서 임포트 시스 써서 해결했더니 메모리 초과남;;; 우째 이거;; 
import sys

sys.setrecursionlimit(10**6)

di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

def dfs(r, c):
    visited[r][c] = 1
    
    for k in range(8):
        nr = r + di[k]
        nc = c + dj[k]
        if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] == 1 and visited[nr][nc]!= 1: 
            # 나는 처음에  0 <= nr < w and 0 <= nc < h 했는데 범위 오류나서 바꿔줬더니 맞았어 근데 왜 그런지 모르겠어.. 알려줄 사람 구함   
            dfs(nr,nc)
             

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0: # 둘 다 0 이 나오면 끝내줘야 하므로 break 
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w  for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                dfs(i,j)

    print(cnt)
