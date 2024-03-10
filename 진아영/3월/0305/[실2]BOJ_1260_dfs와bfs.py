# 111476KB 160ms

N, M, V = map(int, input().split())  # 노드 수, 간선 수, 탐색 시작 번호
adjl = [[] for _ in range(N + 1)]
visited_1 = [0] * (N + 1)
visited_2 = [0] * (N + 1)
q = []

for _ in range(M):
    a, b = map(int, input().split())
    adjl[b].append(a)
    adjl[a].append(b)

adjl = list(map(sorted, adjl))

def dfs(i):
    visited_1[i] = 1     # 방문표시
    print(i, end = ' ')
    lst = adjl[i]        # 그 노드와 연결된 노드 리스트

    for j in lst:
        if not visited_1[j]:   # 연결 노드중 방문하지 않은 노드
            dfs(j)             # dfs 재귀

def bfs(i):
    q = []
    q.append(i)       # q에 첫 노드 append
    visited_2[i] = 1  # 방문표시
    while q:          # 너비우선탐색할 노드가 없을때까지
        a = q.pop(0)
        print(a, end = ' ')
        for j in adjl[a]:    # 그 노드와 연결된 노드 리스트
            if not visited_2[j]:    # 연결 노드중 방문하지 않은 노드
                visited_2[j] = 1    # 방문표시 해주고
                q.append(j)         # 그 노드와 연결된 노드 리스트 검색하기 위해 q에 append

dfs(V)
print()
bfs(V)




#---------------------------------수정 전---------------------------------------------------------
N, M, V = map(int, input().split())  # 노드 수, 간선 수, 탐색 시작 번호
adjl = [[] for _ in range(N + 1)]
visited_1 = [0] * (N + 1)
visited_2 = [0] * (N + 1)
q = []

for _ in range(M):
    a, b = map(int, input().split())
    adjl[b].append(a)
    adjl[a].append(b)

adjl = list(map(sorted, adjl))   # 연결 간선이 여러개인 경우 노드 번호가 낮은거부터 가라고 해서 간선 연결한 후에 다 정렬해줌

def dfs(i):
    visited_1[i] = 1            # 방문표시
    print(i, end = ' ')         # 출력
    lst = adjl[i]               # 연결된 노드 리스트 뽑아옴

    for j in lst:               # 그 리스트에서 하나씩 뽑아서 깊이우선탐색
        if not visited_1[j]:
            dfs(j)

def bfs(i):
    visited_2[i] = 1           # 방문표시
    print(i, end = ' ')        # 출력
    lst = adjl[i]              # 연결된 노드 리스트 뽑아옴
    for j in lst:              # 그 리스트에서 하나씩 뽑아서 큐에 쌓아줌
        q.append(j)

    while q:                   # 그리고 그 큐가 다 빌때까지
        k = q.pop(0)           # 하나씩 뽑아서
        if not visited_2[k]:   # 방문하지 않았으면 너비우선탐색
            bfs(k)

dfs(V)
print()
bfs(V)
