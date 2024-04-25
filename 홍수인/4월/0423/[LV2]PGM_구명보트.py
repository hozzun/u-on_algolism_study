# 처음에 deque안썼더니 하나 시초나서 deque으로 바꿔줌 !

from collections import deque

def solution(people_l, limit):
    answer = 0
    people_l.sort()
    people = deque(people_l)
    
    while len(people) > 1:
        max_weight = people.pop()
        if max_weight + people[0] <= limit:    # 가장 무거운 마지막 무게 + 가장 가벼운 0번째 무게가 limit보다 작으면 둘 다 지우고 ans+1
            people.popleft()
        answer += 1
    if len(people) == 1:   # 한 사람 남으면 answer += 1
        answer += 1
        
    return answer
