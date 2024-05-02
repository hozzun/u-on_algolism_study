# dfs bfs 둘다 시간초과.. dp문제인가 -> 했는데 아니었음! 호준오빠 코드 훔쳐봄 천재네


# bfs ----------------------------------------------------------

from collections import deque

def game(N, arr):
    max_score = 0
    Q = deque()
    
    for idx in range(4):
        score = arr[0][idx]
        Q.append((1, idx, score))
    
    while Q:
        i, b_idx, b_score = Q.popleft()
        
        if i == N:
            max_score = max(max_score, b_score)
            continue
            
        if b_score + (N-i) * 100 <= max_score:
            continue
            
        for idx in range(4):
            if idx != b_idx:
                Q.append((i + 1, idx, b_score + arr[i][idx]))
                
    return max_score
        
        
    
def solution(land):
    answer = game(len(land), land)

    return answer

# dfs --------------------------------------------------------------

def game(i, before_idx, score, land):
    global max_score, N
    
    if i == N:
        max_score = max(max_score, score)
        return
        
    elif i == 0:
        for idx in range(4):
            game(i + 1, idx, score + land[i][idx], land)
            
    else:
        for idx in range(4):
            if idx != before_idx:
                game(i + 1, idx, score + land[i][idx], land)
        
    
def solution(land):
    global max_score, N
    
    max_score = 0
    N = len(land)
    
    game(0, 0, 0, land)

    return max_score
