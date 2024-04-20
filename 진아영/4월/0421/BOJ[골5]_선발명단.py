# 파이썬    31120 kb, 100 ms
# 파이파이 111584 kb, 180 ms

def pos(i, cur_stat):   # 포지션 정할 선수 번호, 능력치
    global max_stat
  
    # 11번선수까지 포지션 정했으면 능력치 비교
    if i == 11:
        max_stat = max(cur_stat, max_stat)

    # 11개의 포지션중 하나 선택해서 재귀
    for p in range(11):
        if not used[p] and stats[i][p] != 0:  # 능력치가 0이 아닌 경우에
            used[p] = 1                       # 포지션 배정 표시
            pos(i+1, cur_stat + stats[i][p])  # 다음 선수로
            used[p] = 0                       # 포지션 배정 초기화

for tc in range(1, 1+int(input())):
    stats = [list(map(int, input().split())) for _ in range(11)]
    used = [0] * 11
    max_stat = 0
    pos(0, 0)

    print(max_stat)
