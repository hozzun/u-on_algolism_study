# Python 메모리: 34640KB, 시간: 100ms, 코드 길이: 527B

from collections import deque

def bfs(x, cnt):
    global answer

    # bfs
    q = deque()
    q.append((x, cnt))
    visited[x] = True # 방문 처리
    while q:
        num, count = q.popleft()
        if num == K: # K랑 같아지면
            answer = min(count, answer) # 최소 시간 저장
            return

        for i in (num - 1, num + 1, num * 2):
            if 0 <= i <= 100000 and not visited[i]: # 범위 안에고 방문 안했던 값이면
                visited[i] = True # 방문 처리
                q.append((i, count + 1)) # 이동


N, K = map(int, input().split())
visited = [False] * 100001
answer = 1e9
bfs(N, 0)

print(answer)
