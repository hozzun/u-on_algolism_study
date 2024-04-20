# 51,064 kb / 1,170 ms

for tc in range(1, 1+int(input())):
    D, L, N = map(int, input().split())
    # 기본데미지, 다음데미지 = D * (1+n*L%), 공격 횟수
    damage = 0

    # 등비수열인가 했는데,,,, 난 그런거 못해....
    for n in range(N):
        damage += (D * (1 + n * L * 0.01))

    print(f'#{tc} {int(damage)}')
