# 50,516 kb, 155 ms

for tc in range(1, 1+int(input())):
    field = list(input())
    ball = 0
    
    for f in range(len(field)):
        if field[f] == '(':          # 왼쪽공 나오면
            ball += 1                # 공 추가
        elif field[f] == ')':        # 오른쪽공 나오면
            if field[f-1] == '(':    # 다 드러난 공이면
                continue             # 패스
            else:                    # 아니면
                ball += 1            # 공추가

    print(f'#{tc} {ball}')
