# 173464 KB, 488 ms

N, M = map(int, input().split())    # 노드 수, 간선 수
visited = [0] * (N + 1)
adjl = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

def dfs(i, c):

    visited[i] = c   # 방문표시를 몇번쨰 깊이우선탐색인지 확인해서 해줌

    lst = adjl[i]

    for j in lst:
        if not visited[j]:
            dfs(j, c)

time = 0   # 몇번째 깊이우선탐색인지 체크

for s in range(1, N + 1):   # 모든 노드 검사해봄..
    if not visited[s]:
        time += 1           # 새로 시작하는 깊이우선 탐색마다 번호 매겨서 검사
        dfs(s, time)

print(time)
