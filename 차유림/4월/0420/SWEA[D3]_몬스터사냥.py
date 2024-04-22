# 51,056 kb / 1,159 ms / 211
T = int(input())
for tc in range(1, T+1):
    D, L, N = map(int, input().split())
    demage = 0
    for i in range(N):
        demage += D + (L * D/100 * i)
    demage = int(demage)
    print(f"#{tc} {demage}")
