메모리 108080 KB, 시간 108 ms

# 인풋 두개
bingo = [list(map(int, input().split())) for _ in range(5)]
check = [list(map(int, input().split())) for _ in range(5)]

# 빙고체크 함수
def bingo_check():
    bingo_num = 0

    # 열체크
    for r in range(5):
        zero_check = 0
        for c in range(5):
            if bingo[r][c] == 0:
                zero_check += 1
            else:
                break
        if zero_check == 5:
            bingo_num += 1

    # 행체크
    for r in range(5):
        zero_check = 0
        for c in range(5):
            if bingo[c][r] == 0:
                zero_check += 1
            else:
                break
        if zero_check == 5:
            bingo_num += 1

    # 대각선 오른쪽 체크
    zero_check = 0
    for r in range(5):
        if bingo[r][r] == 0:
            zero_check += 1
        else:
            break
    if zero_check == 5:
        bingo_num += 1

    # 대각선 왼쪽 체크
    zero_check = 0
    for r in range(5):
        if bingo[r][5 - r - 1] == 0:
            zero_check += 1
        else:
            break
    if zero_check == 5:
        bingo_num += 1

  # 다 하고나서 빙고가 세개 이상이면 완성!
    if bingo_num >= 3:
        return True
    else:
        return False

# 게임 시작 함수
def game(arr_1, arr_2):
    shout = 0
    for i in range(5):
        for j in range(5):
            # 빙고판에서 하나씩 지움
            num = arr_1[i][j]
            shout += 1
            for a in range(5):
                for b in range(5):
                    if arr_2[a][b] == num:
                        arr_2[a][b] = 0
                        if bingo_check():
                            return shout

print(game(check, bingo))
