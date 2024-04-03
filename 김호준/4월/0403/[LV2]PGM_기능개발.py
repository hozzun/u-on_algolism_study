# 엄청난 빡침이 오른다
# 저 라이브러리 하나쓴다고 맞네; 내 아까운 시간
# 올림 round, int 말고 구글링해보다가 ceil 이라는 올림함수를 알게됨 저거 쓰니까 맞네;
# => 스택 문제인데 걍 구현으로 푼듯

from math import ceil # 올림 함수 (라이브러리)
# 대신 무조건 올림
# ex)  2.1 => 3 

def solution(progresses, speeds):
    answer = []
    
    count = ceil((100 - progresses[0]) / speeds[0]) # 기본 0번째 남은 % 값으로 변수 설정
    cnt = 1
    for i in range(1, len(progresses)): # 다음 인덱스부터
        ans = ceil((100 - progresses[i]) / speeds[i]) # 다음 인덱스 % 값
      
        if count >= ans: # 전에 꺼보다 작으면
            cnt += 1 # 횟수 1 증가
          
        elif count < ans: # 클 때는
            count = ans # 기본 변수 바꿔주고
            answer.append(cnt) # 리스트에 넣어줌
            cnt = 1 # 카운트는 리셋
          
        if i == len(progresses)-1: # 끝에 도달하면
            answer.append(cnt) # 지금까지꺼 넣어줌
    
    return answer


# -----------------------------------------------------------------------------------------
# 실패 ( 90.9점, 반올림 문젠데 해결법을 모르겠음 )
# ans에 + 1 하면 10번이 틀리고, 그냥 두면 2번이 틀림
# round, int 별짓 다하면서 1시간 30분 넘게 시도해본듯
def solution(progresses, speeds):
    answer = []
    
    count = (100 - progresses[0]) // speeds[0]
    cnt = 1
    for i in range(1, len(progresses)):
        ans = (100 - progresses[i]) // speeds[i]
        if count >= ans:
            cnt += 1
          
        elif count < ans:
            count = ans
            answer.append(cnt)
            cnt = 1
          
        if i == len(progresses)-1:
            answer.append(cnt)
    
    return answer
