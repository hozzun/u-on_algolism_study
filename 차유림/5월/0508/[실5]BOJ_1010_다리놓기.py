# 백준 실5 1010번 다리 놓기 
# 메모리 31120 kb 시간 80ms 코드길이 345
# 조합을 사용해 구함 mCn = m! / n! (m-n)! 
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    up = 1
    down1 = 1
    down2 = 1
    for i in range(1, M + 1):
        up = i * up
    
    for j in range(1, N + 1):
        down1 = j * down1

    for k in range(1, M - N + 1):
        down2 = k * down2

    bridge = up // (down1 * down2)
    print(bridge)

# # 실패 버전 시간초과 ....... 재귀를 사용해서 그런듯 
def comb(n, r):
    if r == 0 or n == r:
        return 1
    return comb(n-1, r-1) + comb(n-1, r)
    
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    bridge = comb(M, N)
    print(bridge)

# 더 짧은 버전 팩토리얼 메소드?? 사용 
import math
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    bridge = math.factorial(M) // (math.factorial(N) * math.factorial(M-N))
    print(bridge)
