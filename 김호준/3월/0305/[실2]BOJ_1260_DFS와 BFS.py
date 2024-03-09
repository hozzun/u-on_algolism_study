# Python 메모리: 39512KB, 시간: 536ms, 코드 길이: 736B

from collections import deque

def dfs(x):
    visited1[x] = True # 처음 값 방문 처리
    print(x, end=' ') # 도는 값 출력
    for i in range(1, N+1): 
        if not visited1[i] and graph[x][i]: # 방문 안했고 그래프 안에 값이 있을 때만
            dfs(i) # 돌아라


def bfs(x):
    q = deque([x]) # 처음 값 덱에 넣고
    visited2[x] = True # 방문 처리
    while q: # 빌 때 까지 돌아라
        val = q.popleft() # 값 빼서
        print(val, end=' ') # 돌면서 값 출력
        for i in range(1, N+1):
            if not visited2[i] and graph[val][i]: # 위와 동일
                q.append(i) # 넣고
                visited2[i] = True # 방문 처리


N, M, V = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)]

for i in range(M):
    node1, node2 = map(int, input().split())
    graph[node1][node2] = True # 양방향 처리 해주기
    graph[node2][node1] = True

visited1 = [False] * (N+1) # dfs 방문
visited2 = [False] * (N+1) # bfs 방문

dfs(V)
print()
bfs(V)
