from collections import deque

def solution(numbers, target):
    ans = 0
    Q = deque()
    Q.append((0, 0))
    
    while Q:
        tmp, cnt = Q.popleft()   # tmp: 중간 연산 결과 저장하기 위한 변수, cnt : 연산 횟수 누적
        
        if cnt == len(numbers):   # numbers의 모든 숫자를 사용하였으면
            if tmp == target:     # 그 결과가 target과 같은지 확인
                ans += 1          # target과 같으면 최종 결과(ans) += 1
            else:              # target이 아니라면 continue
                continue
        
        else:     # 연산 아직 다 안했으면
            Q.append((tmp+numbers[cnt], cnt+1))    # +, - 두가지 연산하여 Q에 append / cnt += 1
            Q.append((tmp-numbers[cnt], cnt+1))
    return ans
