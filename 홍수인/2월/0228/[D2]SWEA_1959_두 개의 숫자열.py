# 메모리 43772 / 시간 104ms

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_val = 0
    

    for i in range(abs(m-n)+1):
        sum_val = 0
        if m-n > 0:     # m > n 경우
            for j in range(n):
                sum_val += a[j] * b[i+j]
        else:         # m < n 경우
            for j in range(m):
                sum_val += b[j] * a[i+j]
        if sum_val > max_val:
            max_val = sum_val

    print(f'#{tc}', max_val)
