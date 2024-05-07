# 34132 KB, 72 ms

from collections import deque

gears = [list(map(int, input())) for _ in range(4)]
score = 0

for _ in range(int(input())):
    num, turn = map(int, input().split())
    Q = deque()
    Q.append((num-1, turn))  # 옆자리 검사가 필요한 톱니바퀴 Q
    turn_gears = []          # 돌려줘야할 톱니바퀴 정보
    turn_gears.append((num-1, turn))

    while Q:
        cur_num, cur_turn = Q.popleft()
        cur_r, cur_l = gears[cur_num][2], gears[cur_num][6]  # 오른쪽, 왼쪽의 톱니 상태

        for n in [-1, 1]:       # 옆 톱니바퀴 검사
            next = cur_num + n

            # 왼쪽 톱니바퀴일 경우
            if 0 <= next < 4 and n == -1:                                                  # 톱니바퀴 범위 (0~3번)를 벗어나지 않으면서
                if gears[next][2] != cur_l and (next, cur_turn * (-1)) not in turn_gears:  # 톱니가 움직일 수 있고 (n-s극), 돌릴 톱니바퀴 목록에 없으면
                    turn_gears.append((next, cur_turn * (-1)))                             # (톱니바퀴 번호, 방향) Q랑 돌릴 톱니바퀴 목록에 append
                    Q.append((next, cur_turn * (-1)))
                  
            # 오른쪽 톱니바퀴일 경우
            if 0 <= next < 4 and n == 1:
                if gears[next][6] != cur_r and (next, cur_turn * (-1)) not in turn_gears:
                    turn_gears.append((next, cur_turn * (-1)))
                    Q.append((next, cur_turn * (-1)))
                    
    # 톱니바퀴 돌리기
    for turn_num, turn_d  in turn_gears:
        if turn_d == 1:
            gears[turn_num] = gears[turn_num][7:] + gears[turn_num][:7]   # 시계방향
        else:
            gears[turn_num] = gears[turn_num][1:] + gears[turn_num][:1]   # 반시계방향

for s in range(4):
    if gears[s][0] == 1:  # 점수 계산
        score += 2 ** s

print(score)
