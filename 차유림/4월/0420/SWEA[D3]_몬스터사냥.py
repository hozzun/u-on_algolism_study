# 51,056 kb / 1,159 ms / 211
T = int(input())
for tc in range(1, T+1):
    D, L, N = map(int, input().split())
    damage = 0
    for i in range(N):
        damage += D + (L * D/100 * i)
    damage = int(damage)
    print(f"#{tc} {damage}")
