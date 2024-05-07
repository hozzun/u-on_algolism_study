# 파이썬     31120 KB,	1148 ms
# 파이파이  111580 KB, 256 ms

N = int(input())
stats = [list(map(int, input().split())) for _ in range(N)]
min_stat = 999999999999999


def make_team(i, start_team, start_stat, link_team, link_stat):   # 현재 팀원 idx, start팀 구성, start팀 능력치, link팀 구성, link팀 능력치
    global min_stat

    if len(start_team) > N // 2 or len(link_team) > N // 2:    # 팀원 몰리면 return
        return

    if i == N:
        min_stat = min(min_stat, abs(start_stat - link_stat))  # 최솟값 계산
        return

    # 팀원 i가 start 팀에 들어갈 경우 추가될 stat 계산
    new_start = 0
    for s in start_team:
        new_start += stats[s][i]
        new_start += stats[i][s]

    make_team(i + 1, start_team + [i], start_stat + new_start, link_team, link_stat)

    # 팀원 i가 link 팀에 들어갈 경우 추가될 stat 계산
    new_link = 0
    for l in link_team:
        new_link += stats[l][i]
        new_link += stats[i][l]

    make_team(i + 1, start_team, start_stat, link_team + [i], link_stat + new_link)


make_team(0, [], 0, [], 0)

print(min_stat)
