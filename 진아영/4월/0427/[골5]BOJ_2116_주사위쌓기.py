import sys
sys.setrecursionlimit(1000000)


# 맞닿은 숫자대로 주사위 쌓기
def build(i, dice_sum, cur_bottom):  # 지금까지 쌓은 주사위 수, 현재 주사위 최댓값, 현재 bottom 눈의 수
    global max_dice

    if i == N:
        max_dice = max(max_dice, dice_sum)   # 주사위 N개 다 쌓았으면 최댓값 갱신하고 return
        return

    if dice_sum + 6 * (N - i) <= max_dice:   # 시간초과 조건 추가
        return                               # (현재까지의 합에 나머지 눈을 다 6으로 더해도 max보다 작으면 return)

    cur_bottom_idx = dices[i].index(cur_bottom)   # 현재 bottom 인덱스 번호 찾기
    cur_top_idx = dice_dic[str(cur_bottom_idx)]   # 현재 top 인덱스 번호 찾기

    cur_top = dices[i][cur_top_idx]  # 현재 top의 숫자 딕셔너리에서 찾기

    dice = list(range(1, 7))  # 주사위 눈 1~6
    dice.remove(cur_bottom)   # bottom 지우기
    dice.remove(cur_top)      # top 지우기

    cur_dice = max(dice)      # side가 될 값 찾기

    build(i + 1, dice_sum + cur_dice, cur_top)   # 최댓값 더하고 조건대로 주사위 이어서 쌓기




N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
dice_dic = {'0': 5, '1': 3, '2': 4, '3': 1, '4': 2, '5': 0}  # 마주보는 짝 (0 ~ 5 = A ~ F)
max_dice = 0

# 맨 밑 주사위 바닥 숫자 정하기
for cur_bottom_idx in range(6):
    cur_top_idx = dice_dic[str(cur_bottom_idx)]  # 현재 bottom idx와 마주보는 짝 딕셔너리에서 찾기

    cur_bottom = dices[0][cur_bottom_idx]  # 현재 bottom의 숫자 찾기
    cur_top = dices[0][cur_top_idx]        # 현재 top의 숫자 찾기

    dice = list(range(1, 7))  # 주사위 눈은 1~6까지
    dice.remove(cur_bottom)   # 그중에서 bottom 지우기
    dice.remove(cur_top)      # top 지우기

    cur_dice = max(dice)      # 남은 눈 중에서 side 최댓값 찾기
    build(1, cur_dice, cur_top)  # 조건대로 주사위 이어서 쌓기 (위에서 찾은 최댓값 넘기기)


print(max_dice)
