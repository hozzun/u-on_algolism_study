r, c = map(int, input().split())
arr = [[0] * r for _ in range(c)]
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())

    if x == 1:
        arr[0][y-1] = 1
    elif x == 2:
        arr[c-1][y-1] = 1
    elif x == 3:
        arr[y-1][0] = 1
    elif x == 4:
        arr[y-1][c-1] = 1

my_x, my_y = map(int, input().split())
if my_x == 1:
    arr[0][my_y-1] = 2
elif my_x == 2:
    arr[c-1][my_y-1] = 2
elif my_x == 3:
    arr[my_y-1][0] = 2
elif my_x == 4:
    arr[my_y-1][c-1] = 2
    
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
ai, aj = 0, 0
for i in range(c):
    for j in range(r):
        if arr[i][j] == 2:
            ai, aj = i, j
            break

cnt = 0
for k in range(4):
    ni = ai + di[k]
    nj = aj + dj[k]
    '''
    원래는 배열판을 만들어 갈 곳은 1, 본인자리는 2로 두고
    델타로 각 1까지의 거리를 재려고 하였는데,
    이렇게 푸는거 아닌거 같기도하고 + 구현불가 ㅋㅋ
    -> 포기
    '''
