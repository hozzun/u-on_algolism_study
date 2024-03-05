# 백준 1260번 DFS와 BFS 메모리 111488KB, 시간 152ms , 코드길이 660 B

def dfs(i): # i 시작점
    visited1[i] = 1
    print(i, end = ' ')
    for w in sorted(arr[i]):
        # 작은 것 부터 방문하라는 말 못보고 5번 제출함 ㅡㅡ...... 아무튼 연결된 정점 리스트를 오름차순으로 정렬함
        if visited1[w] == 0:
            dfs(w)

def bfs(i): # i 시작점
    queue = [] # 큐 생성
    queue.append(i) # 시작점 추가
    visited2[i] = 1 # 시작점 방문표시 해준다
    while queue: # 큐가 비워질 때 까지
        t = queue.pop(0) # 큐의 맨 앞의 요소 빼
        print(t, end = ' ')
        for w in sorted(arr[t]): # t에 인접인 정점 i ( 오름차순으로 정렬 )
            if visited2[w] == 0: # 방문하지 않은 정점이라면
                queue.append(w) # queue에 추가
                visited2[w] = 1 # 방문 표시


N, M, V = map(int, input().split())  # N : 정점 수, M : 간선 수 ,V : 탐색 시잘할 정점 번호
arr = [[] for _ in range(N + 1)] # 연결된 정점 리스트
for _ in range(M):
    n1, n2 = map(int, input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

visited1 = [0] * (N + 1)
visited2 = [0] * (N + 1)
dfs(V)
print()
bfs(V)
