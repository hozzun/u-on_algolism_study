# 안돼ㅜㅜ 먼가 틀림 ㅜ ㅜ
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    bi = list(map(int, input().split()))
    max_v = -9999999
    if N < M:
        for i in range(M-N+1):
            sum_v = 0
            for r in range(N):
                sum_v += ai[r] * bi[r+i] 
            if sum_v > max_v:
                max_v = sum_v
    elif N == M:
        sum_v = 0
        for i in range(N):
            sum_v += ai[i] * bi[i]
        max_v = sum_v
            
    elif N > M:
        for i in range(N- M + 1):
            sum_v = 0
            for r in range(M):
                sum_v += ai[r+i] * bi[r] 
            if sum_v > max_v:
                max_v = sum_v

    print(f"#{tc} {max_v}")
