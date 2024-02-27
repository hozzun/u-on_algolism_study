# 몇번 째에 빙고를 외치는지 못찾겠어

# 빙고판
arr = [list(map(int, input().split())) for _ in range(5)]
result_arr = arr

# 숫자 목록
lst = []
for _ in range(5):
    lst += list(map(int, input().split()))

# 숫자 부르면 빙고판에 그 숫자 0으로 바꿔줌
for i in range(25):
    for x in range(5):
        for y in range(5):
            if lst[i] == arr[x][y]:
                arr[x][y] = 0

answer = 0
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

# 좌 대각선 세기
l_cnt = 0
for i in range(5):
    if arr[i][i] == 0:
        l_cnt += 1
if l_cnt == 5:
    answer += 1

# 우 대각선 세기
r_cnt = 0
for i in range(5):
    if arr[i][4-i] == 0:
        r_cnt += 1
if r_cnt == 5:
    answer += 1

print(answer)
