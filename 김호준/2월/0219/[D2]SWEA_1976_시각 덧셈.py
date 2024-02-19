# 메모리: 58,248KB, 시간: 143ms
T = int(input())
for tc in range(1, T+1):
    time1, minute1, time2, minute2 = map(int, input().split())

    time = time1 + time2 # 시간끼리 더해주고
    minute = minute1 + minute2 # 분끼리 더해주고

    if minute >= 60: # 분이 60이상이면
        time += (minute // 60) # 시간에 몫 추가
        minute = minute - 60 # 분은 60 빼주고

    if time > 12: # 시간이 12 초과면
        time -= 12 # 12 빼줘라

    print(f'#{tc} {time} {minute}')
