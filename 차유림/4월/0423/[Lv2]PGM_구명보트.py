# 프로그래머스 구명보트
# 실패버전 ㅠㅠ~  

# people = [70, 50, 80, 50]
# limit = 100 
# people.sort()
# weight = 0
# boat = 0
# for i in people:
#     weight += i
#     if weight > limit:
#         boat += 1
#         break
#     else:
#         boat += 1
        

# print(boat)

 
# 큰 보트 부터 무조건 하나 체크하고 나머지 자리에 작은 수들을 체크해봐야 함
# 아영언니가 알려줌... 처음에는 그냥 냅다 작은 것 부터 더헀더니 틀리는겨~~~ 

def solution(people, limit):
    people.sort(reverse=True) # 큰 순서 대로 정렬 
    left = 0 # 인덱스 0번 젤 왼쪽 ex. 0
    right = len(people) - 1 # 제일 마지막 인덱스 ex.3
    boat = 0 # 보트 

    while left <= right: # (인덱스) 왼쪽이 오른쪽을 넘지 않을 떄까지 반복 
        if people[left] + people[right] <= limit: # 0, 3번째 값 80 + 50 (리미트 넘음) / 2, 3 번째 값 50 + 50 (안 넘음)
            right -= 1 # 오른쪽 옮겨줌 

        left += 1 # 왼쪽 한칸 옮겨주고
        boat += 1 # 배 태워 보냄 
        
    return boat

print(solution([70, 50, 80, 50],100))  
