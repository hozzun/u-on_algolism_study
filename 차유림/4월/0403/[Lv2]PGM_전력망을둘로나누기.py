# idea 주어진 wires 간선들을 하나씩 다 끊어봐서 bfs 해봤을 때, 두 개의 차이가 가장 적은 거를 갱신해주기 
# 한 덩어리가 cnt 라고 하면 나머지 한덩이의 갯수는 n-cnt

from collections import deque

def bfs(i, electric, visited): # i 시작 지점 
    q = deque()
    q.append(i)
    cnt = 1
    visited[i] = 1
    
    while q: # q가 비워질때까지 밑에는 수업시간에 배운 bfs 알고리즘 사용함
        cur = q.popleft()
        for w in electric[cur]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1
                cnt += 1 # 방문하지 않은 지점들을 카운트 해줌 
    return cnt # 카운트 반환
    
def solution(n, wires):
    result = []
    electric = [[] for _ in range(n + 1)] # 간선 정보 저장할 리스트
    for n1, n2 in wires: # 양방향으로 저장해줌 
        electric[n1].append(n2)
        electric[n2].append(n1)
    
    for i, cut in wires: # 시작 지점 , 자를 노드
        visited = [0] * (n + 1)
        visited[cut] = 1
        cnt = bfs(i, electric, visited) 
        result.append(abs(cnt - n + cnt))
        
    return min(result) # result에는 차이가 최소인것만 남게 ... 
