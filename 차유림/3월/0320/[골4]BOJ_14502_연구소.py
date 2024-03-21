# 백준 14502번 연구소 
# thx hj,,,, 알려준대로 했더니 됐어. . .  wow!!!!!! 압도적 감사! ! ! 
# 메모리 127176 kb 시간 2672kb 코길 1152b
from collections import deque
import copy

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
max_val = 0

def wall(cnt):
    if cnt == 3: # 벽이 3개가 된다면 
        virus() # 바이러스 퍼뜨리기 !! 
        return 
    
    for i in range(N): # 돌면서 0 인 부분을 1로 바꿔주고 cnt + 1 해줌 벽은 3개만 세울 수 있다 ! 
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt + 1)
                arr[i][j] = 0 # 이거 안써줬는데 자꾸 답이 이상하게 나옴 !!!! 원래대로 돌려줘야하는걸 자꾸 뺴먹어~~~ ㅜ 자꾸 24, 0, 12?나옴 ㅜㅜ 그래서 참고... 햇음!! 

def virus():
    global max_val
    q = deque()
    wall = copy.deepcopy(arr) # 딥카피해줌 

    for i in range(N): # 다 돌면서 
        for j in range(M):
            if arr[i][j] == 2: # 2인 부분을 큐에 넣음 !! 처음에 그냥 냅다 r, c 넣었다가 뭔가 이상해서 바꿈 q.append((r, c))  
                q.append((i, j))
    
    while q: # q가 다 비워질떄까지 
        r, c = q.popleft()
        for k in range(4): # 2인 부분을 기점으로 4방향 탐색 
            nr = r + di[k]
            nc = c + dj[k]
            if 0 <= nr < N and 0 <= nc < M:
                if wall[nr][nc] == 0: # 만약에 0 인 부분이 있다면 
                    wall[nr][nc] = 2 # 2로 다 바꾸고 
                    q.append((nr, nc)) # q에 넣어줌 

    virus_val = 0 # 벽 3개 세우고 바이러스를 다 퍼뜨렸을 때 0 인 부분 세줄 변수 
    for i in range(N):
        for j in range(M):
            if wall[i][j] == 0:
                virus_val += 1
    
    max_val = max(max_val, virus_val) # max_val 과 virus_val 중에 max 찾아서 넣어줌 

wall(0)

print(max_val)
    
