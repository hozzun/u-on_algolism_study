# 메모리 : 331120 / 시간 : 40ms

a, b = map(int, input().split())
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dong_pos = list(map(int, input().split()))
idx_lst = []    # 입력 받은 정보(arr)을 인덱스로 변환하여 저장
arr.append(dong_pos)    # 마지막 값이 동근이의 위치

for i in arr:
    if i[0] == 1 :   # 1: 북
        idx_lst.append((i[1], 0))
    elif i[0] == 2:    # 남
        idx_lst.append((i[1], b))
    elif i[0] == 3:  # 서
        idx_lst.append((0, i[1]))
    else:    # 동
        idx_lst.append((a, i[1]))
l = 0
x = 0
center_lenth = a+b     # 시계/반시계 거리가 같은 경우 -> 최단경로인지 판별할 때 사용.


# 맞은 편에 있을 경우 : 사이의 길이 + 왼쪽/오른쪽 끝으로부터 각각의 거리
# 인접 변 / 같은 변에 있는 경우 : x좌표, y좌표 간의 차의 합 == 최단 경로

for i in range(n):
    if abs(idx_lst[n][1] - idx_lst[i][1]) == b:    # 북/남 맞은 편  (두 y좌표의 차 == 세로 길이)
        if idx_lst[n][0] + idx_lst[i][0] + b >= center_lenth:     # 시계방향이 최단경로 x
            l += b + 2*a - (idx_lst[n][0] + idx_lst[i][0])              # (가로 변의 마지막 죄표 - 동근이 x좌표) + (가로 변의 마지막 좌표 - i번째 상점 x좌표) + 세로 길이
        else:                                                     # 시계방향이 최단경로 o
            l += b + idx_lst[n][0] + idx_lst[i][0]

    elif abs(idx_lst[n][0] - idx_lst[i][0]) == a:   # 서/동 맞은 편  (두 x좌표의 차 == 가로 길이)
        if idx_lst[n][1] + idx_lst[i][1] + a >= center_lenth:     # 시계방향이 최단경로 x
            l += a + 2*b - (idx_lst[n][1] + idx_lst[i][1])
        else:                                                     # 시계 방향이 최단 경로 o
            l += a + idx_lst[n][1] + idx_lst[i][1]

    else:       # 인접 변 / 같은 변에 위치
        l += (abs(idx_lst[n][0] - idx_lst[i][0]) + abs(idx_lst[n][1] - idx_lst[i][1]))

print(l)
