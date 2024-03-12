# Python 메모리: 31120KB, 시간: 40ms, 코드 길이: 486B

def dfs(y, x):
    if y == N-1 and x == N-1: # 끝에 도달하면
        print('HaruHaru') # HaruHaru 출력하고
        exit(0) # 끝내기

    di = [graph[y][x], 0] # 해당 좌표값 만큼 이동(우, 하)
    dj = [0, graph[y][x]]
    visited[y][x] = True # 방문 처리

    for k in range(2):
        ni = y + di[k]
        nj = x + dj[k]
        if 0 <= ni < N and 0 <= nj < N: # 값이 있는 곳만
            if not visited[ni][nj]: # 방문 안했으면
                dfs(ni, nj) # 계속 돌아봐라



N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dfs(0, 0)
print('Hing') # 디폴트 값 Hing(다 돌았는데 끝에 못갔으면 출력)
