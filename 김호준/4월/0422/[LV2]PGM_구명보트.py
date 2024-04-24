from collections import deque

def solution(people, limit):
    answer = 0
    # 무거운 순서대로 덱으로 만듦
    q = deque(sorted(people, reverse=True))
    
    while len(q) > 1:
        # 가장 무거운 사람 + 가장 가벼운 사람 = limit보다 같거나 작으면
        if q[0] + q[-1] <= limit:
            # 배에 태워 보내고 빼줌
            answer += 1
            q.pop()
            q.popleft()
        # 두 명 무게 넘어가면 가장 무거운 사람만 보내줌  
        else:
            answer += 1
            q.popleft()

    # 홀 수인 경우 1명 남으면 1명도 마저 태워 보내버림 ㅂ2
    if len(q) == 1:
        answer += 1
        
    return answer
