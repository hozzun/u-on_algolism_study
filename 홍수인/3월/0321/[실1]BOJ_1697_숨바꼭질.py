# 메모리: 35656, 시간: 108ms, 코드 길이: 428B

from collections import deque
def bfs(start, end):
    Q = deque()
    v = [0] * 100001    # visited 배열

    Q.append(start)   # 시작점
    v[start] = 1

    while Q:
        c = Q.popleft()
        if c == end:   # 도달하고자 하는 수와 일치하는 경우
            return v[c] - 1    # 연산 횟수 return

        for i in ((c+1), (c-1), (c*2)):
            if 0 <= i <= 100000 and v[i] == 0:  # 범위 포함이면서 이전과 중복되지 않다면
                Q.append(i)
                v[i] = v[c] + 1   # 방문표시 + 연산 횟수 표시


n, k = map(int, input().split())
result = bfs(n, k)
print(result)
