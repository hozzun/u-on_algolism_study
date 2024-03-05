# 31120 KB, 44 ms

N = int(input())  # 노드 수
T = int(input())  # 간선 수

visited = [0] * (N + 1)            # 방문 표시
adj = [[] for _ in range(N + 1)]   # 연결 노드 리스트

for _ in range(T):
    a, b = map(int, input().split())
    adj[a].append(b)   # 노드 양방향 연결
    adj[b].append(a)

def dfs(i):
    lst = adj[i]
    visited[i] = 1   # 방문 표시

    for j in lst:
        if not visited[j]:   # 연결 노드 리스트에서 하나씩 뽑아서 재귀
            dfs(j)

dfs(1)

print(visited.count(1) - 1)   # 1 빼고 출력
