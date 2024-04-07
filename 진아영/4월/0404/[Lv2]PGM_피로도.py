# 100점

# 처음에 순열로 돌려서 하려다가 시간초과나서 이틀 지나고 새로운 마음으로 다시 풀어봄
# 다시할때는 그때그때 선택할때마다 갱신해줌


def explore(cur_k, i, dungeons):  # 현재 피로도, 탐험 동굴 수, 던전 리스트
    global max_e, explored
    
    max_e = max(i, max_e)
    
        
    # 현재 인덱스 탐험하는 경우
    for j in range(len(dungeons)):
        if not explored[j] and dungeons[j][0] <= cur_k:
                explored[j] = 1
                explore(cur_k - dungeons[j][1], i+1, dungeons)
                explored[j] = 0
    return
    


def solution(k, dungeons):
    global max_e, explored
    max_e = -1
    
    explored = [0] * (len(dungeons))
    explore(k, 0, dungeons)
    
    return max_e
