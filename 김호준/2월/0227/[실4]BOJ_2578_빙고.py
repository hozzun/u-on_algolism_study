# Python 메모리: 31120KB, 시간: 40ms

def check():
    answer = 0 # 빙고 줄
    # 가로 세기
    for i in range(5):
        cnt = 0
        for j in range(5):
            if arr[i][j] == 0:
                cnt += 1
        if cnt == 5:
            answer += 1

    # 세로 세기
    for i in range(5):
        cnt = 0
        for j in range(5):
            if arr[j][i] == 0:
                cnt += 1
        if cnt == 5:
            answer += 1

    # 좌 대각선 세기 \
    l_cnt = 0
    for i in range(5):
        if arr[i][i] == 0:
            l_cnt += 1
    if l_cnt == 5:
        answer += 1

    # 우 대각선 세기 /
    r_cnt = 0
    for i in range(5):
        if arr[i][4 - i] == 0:
            r_cnt += 1
    if r_cnt == 5:
        answer += 1

    return answer # 내보내주고


# 빙고판
arr = [list(map(int, input().split())) for _ in range(5)]

# 숫자 목록
lst = []
for _ in range(5):
    lst += list(map(int, input().split()))

# 숫자 부르면 빙고판에 그 숫자 0으로 바꿔주고 횟수 셈
cnt = 0
for i in range(25):
    for x in range(5):
        for y in range(5):
            if lst[i] == arr[x][y]:
                arr[x][y] = 0
                cnt += 1

    if cnt >= 12: # 양 대각선 + 한줄 하면 최소 12임 == 최소 3줄이면
        result = check() # 체크함수 발동

        if result >= 3: # 최소 숫자 12개에 3줄되었다면
            print(i + 1) # 출력
            break
