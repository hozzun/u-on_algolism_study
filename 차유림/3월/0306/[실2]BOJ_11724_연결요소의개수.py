# 백준 11724번 연결 요소의 개수
# 메모리 : 173484KB 시간 476ms 길이: 433B
N, M = map(int, input().split())  # N: 정점의 갯수 M : 간선의 갯수
arr = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 0
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

def dfs(i):
    visited[i] = 1
    for w in arr[i]:
        if visited[w] == 0:
            dfs(w)

for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)
