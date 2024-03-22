# 파이썬    35320 KB, 104 ms, 666 B
# 파이파이 115912 KB, 148 ms


from collections import deque

def move(i):

    global min_time

    Q = deque()
    visited = [0] * 100001    # 몇초 걸렸는지 저장
    Q.append(i)
    visited[i] = 1

    while Q:
        cur = Q.popleft()

        if cur == finish:                   # 도착지점에 도착하면
            if visited[cur] < min_time:     # 최소값 저장하고
                min_time = visited[cur]
            return                          # return

        next_c = [cur+1, cur-1, cur*2]    # 다음 이동 리스트
        for j in next_c:
            if 0 <= j <= 100000 and not visited[j]:    # 방문하지 않은 곳이고 범위 안에 있으면
                visited[j] = visited[cur] + 1          # 걸린 시간 저장
                Q.append(j)



start, finish = map(int, input().split())

min_time = 999999999999999999999999
move(start)

print(min_time-1)
