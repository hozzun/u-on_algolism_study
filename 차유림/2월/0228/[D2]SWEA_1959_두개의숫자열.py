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

# max_v 값 바꿔줫더니 된다~~ 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    bi = list(map(int, input().split()))
    max_v = -9999999 # 원래 숫자를 엄청 작게 해놨었는데 그래서 런타임에러난듯 ;; 조금 더 큰수로 바꾸니까 됐당..
    
    if N < M: # 길이별로 조건문 작성 n < m 일 때 
        for i in range(M - N + 1):
            sum_v = 0
            for j in range(N):
                sum_v += ai[j] * bi[i + j]
            if max_v < sum_v:
                max_v = sum_v
    elif N == M: # n = m일 때
        sum_v = 0
        for i in range(N):
            sum_v += ai[i] * bi[i] # 그냥 요소마다 곱해줘서 sum_v에 저장 
        if max_v < sum_v:
            max_v = sum_v
    
    elif N > M: # n > m 일 때 
        for i in range(N - M + 1):
            sum_v = 0
            for j in range(M):
                sum_v += ai[i + j] * bi[j]
            if max_v < sum_v:
                max_v = sum_v

    print(f"#{tc} {max_v}")
    
