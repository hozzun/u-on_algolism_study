# 100점 / 그냥 무난한 완탐 문제인듯

def recur(k, dungeons, visited, cnt):
    global answer
    if cnt > answer: # cnt가 클때마다 갱신
        answer = cnt
    
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]: # 하나씩 돌아보면서 만약 방문안했고, 피로도 충분하면
            visited[i] = True # 방문
            recur(k - dungeons[i][1], dungeons, visited, cnt + 1) # 돌아봐라
            visited[i] = False # 백트래킹

def solution(k, dungeons):
    global answer
    answer = -1
    
    visited = [False] * len(dungeons) # 다 돌아봐야하기 때문에 visited 생성
    recur(k, dungeons, visited, 0) # 완탐
    return answer
