메모리 : 34072, 시간 : 460ms 코드 길이 : 41

from collections import deque

def dfs(q):
    global result_dfs
    visited[q] = 1
    result_dfs.append(q)
    for w in graph[q]:
        if visited[w] == 0:
            dfs(w)

def bfs(q):
    global result_bfs
    while Q:
        c = Q.popleft()
        result_bfs.append(c)
        for w in graph[c]:    # Q에서 꺼낸 노드의 인접 정점이 방문하지 않은 상태라면, Q에 append, 방문표시
            if visited[w] == 0:
                Q.append(w)
                visited[w] = 1

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
result_dfs = []
result_bfs = []
for _ in range(m):    # 그래프 형성
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)   # 양방향

for i in graph:   # 숫자가 작은 노드부터 방문하므로 오름차순 정렬.
    i.sort()

# dfs
dfs(v)
print(*result_dfs)

# bfs
visited = [0] * (n+1)    # visited 초기화
visited[v] = 1         # 시작점 방문표시
Q = deque([v])
bfs(v)
print(*result_bfs)
