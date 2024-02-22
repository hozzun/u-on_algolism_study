# 메모리 : 43,760 kb 시간 : 103 ms
# idea : 인덱스 활용과 조건 잘 사용하기.
T = int(input())
for tc in range(1, T+1):
    time_list = list(map(int, input().split()))

    hour = time_list[0] + time_list[2] # 시 따로 분 따로 저장
    minute = time_list[1] + time_list[3]
    if minute > 60: #분 60 넘어가면 시에 1 더해주고~
        hour += 1
        minute = (minute - 60)
    if hour > 12: #시가 12 넘어가면 12를 빼서 시계형식으로 만들어주고~
        hour = hour - 12
    print(f'#{tc} {hour} {minute}')
