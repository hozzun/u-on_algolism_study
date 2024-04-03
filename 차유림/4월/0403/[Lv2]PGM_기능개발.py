def solution(progresses, speeds):
    answer = []
    cnt = 0 # 배포하는 거 카운트 해줌
    time = 0 # 걸리는 시간
    while progresses: # progresses 빌 때까지
        if (progresses[0] + time * speeds[0]) >= 100: # 계속 값을 증가시키다가 100보다 커지면
            cnt += 1 # 카운트 1해줌
            progresses.pop(0) # 왼쪽값 제거
            speeds.pop(0)
        else: # 값이 100 미만일때
            time += 1 # 횟수를 계속 늘려줌
            if cnt > 0: # 카운트가 0보다 크다면 
                answer.append(cnt) # answer에 넣어줌
                cnt = 0 # 다시 초기화 

    answer.append(cnt) # 마지막 값 안들어가서 넣어줬음!! 
            
    return answer
