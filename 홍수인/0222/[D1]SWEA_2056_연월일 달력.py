# 메모리 45076 / 실행시간 100ms

t = int(input())
for case in range(1, t+1):
    c = input()

    # 날짜가 유효하지 않는 경우
    # 달이 12이상 or 0인 경우
    if int(c[4:6]) > 13 or int(c[4:6]) == 0:
        print(f'#{case} -1')
    # 31일까지인 달
    elif (int(c[4:6]) == 1 or 3 or 5 or 7 or 8 or 10 or 12) and int(c[6:8]) > 31:
        print(f'#{case} -1')
    # 30일까지인 달
    elif (int(c[4:6]) == 4 or 6 or 9 or 11) and (int(c[6:8]) > 30):
        print(f'#{case} -1')
    # 2월
    elif (int(c[4:6]) == 2) and (int(c[6:8]) > 28):
        print(f'#{case} -1')
        
    # 날짜가 유효한 경우
    else:
        y = c[0:4]
        m = c[4:6]
        d = c[6:8]
        print(f'#{case} {y}/{m}/{d}')
