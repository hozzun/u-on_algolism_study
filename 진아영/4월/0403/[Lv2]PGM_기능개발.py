# 100점

from collections import deque

def solution(progresses, speeds):
    
    progresses = deque(progresses)   # 덱으로 변환
    speeds = deque(speeds)
    answer = []
    d = 0   # 배포 가능 수
    
    while progresses:
        
        for i in range(len(progresses)):    # 인덱스별로 하나씩 더하기
            progresses[i] += speeds[i]
        
        while progresses:
            if progresses[0] >= 100:        # 그 결과 100이 넘었으면
                progresses.popleft()        # popleft
                speeds.popleft()
                d += 1                      # 배포 가능 수 늘려주기
            else:                           # 젤 왼쪽이 100 안넘었으면
                if d > 0:                   # 배포 가능한게 있는지 확인하고
                    answer.append(d)        # 가능하면 answer에 append
                    d = 0                   # 배포 완료 했으니까 초기화
                break                       # 안쪽 while 끄고 젤 바깥쪽 while 다시 시작
                
    if not progresses and d:                # 다 pop 했을때 배포가능한게 있는지 확인하고
        answer.append(d)                    # 있으면 append
    
    return answer
