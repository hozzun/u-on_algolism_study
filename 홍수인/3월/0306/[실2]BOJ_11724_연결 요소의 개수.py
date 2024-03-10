메모리 : 169480, 시간 : 340ms, 코드 길이 : 25

def dfs(v):
    global visited

    visited[v] = 1
    for w in graph[v]:
        if visited[w] == 0:
            visited[w] = 1
            dfs(w)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
visited[0] = 1
cnt = 0

for i in range(m):     # 그래프 형성
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

while visited.count(0) > 0:  # 모든 노드 방문할 때 까지 반복.
    cnt += 1    # dfs 함수 실행 이후에도 방문하지 않은 정점이 존재한다면 cnt += 1
    dfs(visited.index(0))    # 방문하지 않은 노드를 시작으로 dfs 재호출.

print(cnt)
