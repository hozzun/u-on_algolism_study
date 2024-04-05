def solution(progresses, speeds):
    n = len(progresses)
    answer = []
    day = []    # 걸리는 시간 계산한 결과
    for i in range(n):
        if (100-progresses[i])%speeds[i] == 0:
            day.append(round(100-progresses[i])//speeds[i])
        else:
            day.append(round(100-progresses[i])//speeds[i]+1)
    
    index= 0
    
    for i in range(len(day)):
        if day[index] < day[i]:   # 뒤의 값이 더 크다면
            answer.append(i - index)   # 개수 answer에 append
            index = i   # index값은 배포된 다음 것으로 갱신
    answer.append(len(day) - index)    # 마지막 처리
    
    return answer

#------------------------------------------------------------------------------------------------------
## 실패 버전 ))) 세개만 맞은 답...
  # 다음 인덱스의 값이 더 작으면 cnt 누적하고 다음 인덱스의 값이 더 클 경우 이 누적한 값을 answer list에 저장 하려고 했으나 틀림;
    # cnt = 1
    # for i in range(n):
    #     if i == n-1:   # 마지막 인덱스이면 지금까지의 cnt append
    #         answer.append(cnt)
    #     else:
    #         if day[i]-day[i+1] < 0:
    #             answer.append(cnt)
    #             cnt = 1
    #         else:
    #             cnt += 1
