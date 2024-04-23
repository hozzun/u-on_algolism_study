# 백준 3980 번 선발명단 
# 31120 / 144 / 513 

def dfs(player, score):                                        # 현재 플레이어 , 현재 점수 
    global max_score
    
    if player == 11:                                            # 11이 될 때 까지 
        max_score = max(max_score, score)                       # 최대값이 갱신된다면 계속 바꿔줌 
        return 
    
    for i in range(11):
        if player_check[i] == 0 and arr[player][i] != 0:        # 플레이어 체크한 리스트가 0 이고 arr 값이 0 이 아닌 것만 탐색해야함
            player_check[i] = 1                                 # 1로 체크해줌 
            dfs(player + 1, score + arr[player][i])             # 재귀 player + 1 해주고 score 에는 점수를 더해줌 2차원 배열이므로 player행 의 i 번째 열
            player_check[i] = 0                                 # 초기화 


C = int(input())
for _ in range(C):
    arr = [list(map(int, input().split())) for _ in range(11)]
    max_score = 0
    player_check = [0] * 11
    dfs(0, 0)
    print(max_score)
