메모리: 31120, 시간 48ms, 코드길이 19

def dfs(v):
    visited[v] = 1
    for m in lst[v]:   # 1번 노드와 연결된 노드 중 방문하지 않은 곳 -> bfs 호출
        if visited[m] == 0:
            dfs(m)

n = int(input())
w = int(input())

lst = [[] for _ in range(n+1)]   # 그래프 생성.
for i in range(w):
    start, end = map(int, input().split())
    lst[start].append(end)
    lst[end].append(start)   # 양방향

visited = [0 for _ in range(n+1)]
visited[1] = 1   # 시작노드 : 1 -> 방문표시
dfs(1)
print(sum(visited)-1)   # 시작노드 1번 제외
