# 백준 2606번 바이러스
# 메모리 31120KB 시간 48ms 코드길이 367B

def dfs(i): # i : 시작 노드
    global cnt
    visited[i] = 1
    # print(i) => 1 2 3 5 6 이 나옴 그래서 1번애 연결된것이 4개이므로 4를 출력해야 함
    for w in arr[i]:
        if visited[w] == 0:
            cnt += 1 # 만약 탐색이 성공했을 때 cnt에 1을 증가시켜줬음
            dfs(w)
    return cnt

V = int(input()) # 노드 수 
E = int(input()) # 간선 수
arr = [[] for _ in range(V+1)] # 인접리스트
for _ in range(E):
    n1, n2 = map(int, input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

cnt = 0
visited = [0] * (V + 1)
print(dfs(1))
