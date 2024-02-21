# 메모리 58,528 kb 시간 155 ms


def calendar_check(y, m, d):
    b, c = int(m), int(d)

    # 월 조건, 일 조건 체크
    if b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12:
        if c < 1 or 31 < c:
            return -1
    elif b == 4 or b == 6 or b == 9 or b == 11:
        if c < 1 or 30 < c:
            return -1
    elif b == 2:
        if c < 1 or 28 < c:
            return -1
        
    # 월이 해당 숫자에 해당하지 않으면 -1
    else:
        return -1
    
    return f'{y}/{m}/{d}'

for tc in range(1, 1+int(input())):
    N = input()
    year = N[:4]
    month = N[4:6]
    day = N[6:8]
    print(f'#{tc} {calendar_check(year, month, day)}')
    
