T = int(input())

for tc in range(1, T+1):
    d, l, n = map(int, input().split())
    dmg = 0
    for i in range(n):
        dmg += d * (1 + i * l / 100)  # i번째의 데미지값 구해서 누적합
    print(f'#{tc}', int(dmg))
