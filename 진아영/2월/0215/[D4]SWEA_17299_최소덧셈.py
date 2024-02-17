for tc in range(1, 1 + int(input())):
    N = input()
    n = len(N)
    min_sum = 99999999999999999

    for i in range(1, n):
        if min_sum > int(N[:i]) + int(N[i:]):     # 슬라이싱으로 문자열 자르기
            min_sum = int(N[:i]) + int(N[i:])

    print(f'#{tc} {min_sum}')
