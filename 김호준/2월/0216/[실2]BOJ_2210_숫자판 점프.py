di = [0, 1, 0, -1] # 네 방향 이동을 위한 델타
dj = [1, 0, -1, 0]

def dfs(x, y, make): # bfs로 해보려 하였으나, 문자열로 해야해서 실패
    if len(make) == 6: # make에 6자리가 다 붙으면
        if make not in result: # result 리스트에 없는거면
            result.append(make) # 넣어라
            return

    else:
        for i in range(4):
            ni = x + di[i] # 방향
            nj = y + dj[i] # 방향
            if 0 <= ni < 5 and 0 <= nj < 5: # range5라서 4까지
                dfs(ni, nj, make + arr[ni][nj]) # 바꾼거로 계속 재귀

arr = [list(map(str, input().split())) for _ in range(5)] # 입력(int로 첨에했다 계속 더해져서 문자열로)
result = [] # 6자리 모으는 리스트
for i in range(5): # 입력 5x5 배열 돌리는 함수 인자용도 + ni, nj 안에 x, y 변수
    for j in range(5):
        dfs(i, j, arr[i][j]) # 함수 호출

print(len(result)) # result 길이
