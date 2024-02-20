# 42,192 kb 103 ms
T = int(input())
for tc in range(1, T+1):
    yyyymmdd = input()
    mm_31 = [1,3,5,7,8,10,12] # 31, 30, 28일 월 구별
    mm_30 = [4,6,9,11]
    mm = int(yyyymmdd[4:6]) #슬라이싱으로 연월일 구별
    dd = int(yyyymmdd[6:])
    answer = 0
    if 0 < mm <= 12:
        if mm in mm_31:
            if 1 <= dd <= 31:
                answer = 1
        elif mm in mm_30:
            if 1 <= dd <= 30:
                answer = 1
        elif mm == 2:
            if 1 <= dd <= 28:
                answer = 1

    if answer:
        answer = yyyymmdd[:4]+'/'+yyyymmdd[4:6]+'/'+yyyymmdd[6:]
        print(f'#{tc} {answer}')
    else:
        print(f'#{tc} -1')
