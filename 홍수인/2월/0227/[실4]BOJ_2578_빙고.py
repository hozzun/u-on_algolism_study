def delta(r, c):
    global bingo
    for w in range(5):    # arr의 0번째 행 순회하며 빙고인지 판단.
        r = 0
        c = w
        for i in range(4):   # 4방향
            cnt = 0
            for j in range(5):   # 같은 방향으로 5개가 !인지 체크
                ni = r + di[i] * j
                nj = c + dj[i] * j
                if 0 <= ni < 5 and 0 <= nj < 5 and arr[ni][nj] == '!':
                    cnt += 1
                    if cnt == 5:
                        bingo += 1
                        return
                else:
                    break
                
arr = [list(map(int, input().split())) for _ in range(5)]
num = [list(map(int, input().split())) for _ in range(5)]
result = []
idx_lst = []
bingo = 0

di = [0, 1, 1, 1]
dj = [1, 0, -1, 1]  # 우, 하, 좌하, 우하

for i in range(5):
    for j in range(5):
        for k in range(5):
            for o in range(5):
                if num[i][j] == arr[k][o]:
                    arr[k][o] = '!'
                    delta(0, 0)
                    if bingo == 3:
                        print(i*5 + j-1)
                        break
