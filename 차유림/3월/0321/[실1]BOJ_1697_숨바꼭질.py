# 백준 1697번 숨바꼭질 
# 메모리 34260kb 시간 100ms 코길 469b

from collections import deque

def bfs(num, cnt):
    q = deque()
    q.append((num, cnt)) # (num, cnt) 튜플 형태로 q 에 넣어준다 
    visited[num] = 1 # num 방문 표시 1 

    while q: # q 가 비워질때까지 
        qnum, qcnt = q.popleft() 
        if qnum == K: # qnum 이 K가 되었다면 
            return qcnt # qcnt 리턴 
        
        for n in (qnum + 1, qnum - 1, qnum * 2): # 수빈이는 + 1, -1 , *2 할 수 있음 
            if 0 <= n <= 100000 and visited[n] == 0: 
                visited[n] = 1
                q.append((n, qcnt + 1))


N, K = map(int, input().split())
visited = [0] * 100001
cnt = 0
print(bfs(N, 0))

