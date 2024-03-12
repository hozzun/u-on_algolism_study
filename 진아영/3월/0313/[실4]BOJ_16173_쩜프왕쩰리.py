# 파이썬 34044 KB, 64 ms, 618 B

from collections import deque

N = int(input())
game_map = [list(map(int, input().split())) for _ in range(N)]
di = [1, 0]
dj = [0, 1]

def game(i, j):

    q = deque()
    q.append((i, j))

    while q:
        a = q.popleft()
        if a[0] == N-1 and a[1] == N-1:   # 끝지점이면 return 하루하루
            return 'HaruHaru'
        elif game_map[a[0]][a[1]] == 0:   # finish 위치도 아니고 현재위치가 0이면 더이상 이동 불가능하므로 return 힝
            return 'Hing'                 # 조건 못읽어서 자꾸 83퍼센트에서 멈춤..

        for k in range(2):
            ni = a[0] + di[k] * game_map[a[0]][a[1]]
            nj = a[1] + dj[k] * game_map[a[0]][a[1]]
            if 0 <= ni < N and 0 <= nj < N:
                q.append((ni, nj))
    
    return 'Hing'   # 끝까지 못도달하면 return 힝

print(game(0, 0))
