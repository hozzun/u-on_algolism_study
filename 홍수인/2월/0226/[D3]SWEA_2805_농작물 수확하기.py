# 메모리 63552 / 시간 214ms
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = []

    for j in range(n):
        s = input()
        a = []
        for i in s:
            a.append(int(i))
        arr.append(a)

    sum_val = 0
    
    # 행 0 ~ n//2 (중간행)까지 값 누적
    for i in range(n//2+1):  # 0-n//2
        for j in range(1, i+1):
            sum_val += arr[i][n//2+j] + arr[i][n//2-j]

    # 행 n//2+1 ~ 끝까지 값 누적
    for i in range(n//2+1, n):
        for j in range(n-i-1, 0, -1):
            sum_val += arr[i][n//2+j] + arr[i][n//2-j]

    # 가운데 열 값 누적
    for i in range(n):
        sum_val += arr[i][n//2]

    print(f'#{tc} {sum_val}')
