# 백트래킹으로 풀었는디 .;,,,,, 예제만 맞고 다 틀리네;;;;; dp 래 omg ㅠㅠ !! 그래서? 모르겠음 ㅠㅠ~ 

max_v = -9999999
def game(i, N, sum_v, visited, land):
    global max_v
    if i == N:
        if sum_v > max_v:
            max_v = sum_v
    else:
        for j in range(4):
            if visited[j] == 0:
                visited[j] = 1
                game(i + 1, N, sum_v + land[i][j], visited, land)
                visited[j] = 0
            
def solution(land):
    global max_v
    N = len(land)
    visited = [0] * 4
    game(0, N, 0, visited, land)
    return max_v
