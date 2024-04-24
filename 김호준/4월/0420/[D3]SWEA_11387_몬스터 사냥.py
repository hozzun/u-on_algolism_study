# SWEA 11387 / 메모리: 51324KB, 시간: 1448ms, 코드 길이: 195

# 그냥 문제에 있는대로 함..
T = int(input())
for tc in range(1, T+1):
    D, L, N = map(int, input().split())

    LL = L / 100
    dmg = 0
    for i in range(N):
        dmg += D * (1+i * LL)

    print(f'#{tc}', int(dmg))
