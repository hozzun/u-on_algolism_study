# Python 메모리: 31120KB, 시간: 44ms, 코드 길이: 515B

def dfs(x):
    global a, b, cnt

    if x == b: # 돌다가 b가 되면 cnt 출력
        print(cnt)
        exit(0)

    visited[x] = True # 방문 처리
    for i in range(1, N+1): # 1~N+1 돌면서
        if graph[x][i] and not visited[i]:
            cnt += 1 # 1 증가하고 계속 이동
            dfs(i)
            cnt -= 1 # i가 원하는 길이 아닐 때는 다시 원상복귀 (이거 안해줬다가 틀렸음)


# 입력
N = int(input())
a, b = map(int, input().split())
M = int(input())

# 배열, 방문
graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

# 양방향
for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

cnt = 0
dfs(a) # a부터 시작 b도착하면 cnt 출력
print(-1) # 아닐 시 -1 출력
