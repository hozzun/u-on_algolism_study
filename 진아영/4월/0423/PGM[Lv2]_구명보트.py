def solution(people, limit):
    answer = 0
    people.sort()
    start = 0               # 보트 안 탄 사람들 중 최솟값
    end = len(people) - 1   # 보트 안 탄 사람들 중 최댓값

    while start <= end:   # 원래 deque 사용해서 보트 탄사람 한명씩 remove 했는데 시간초과나서 인덱스 옮기기로 변경
        answer += 1       # 보트 한개 대령
        p1 = people[start]
        p2 = people[end]
        
        if start == end:  # start와 end가 만났으면 사람 다 태웠으므로 break
            break
        
        if p1 + p2 <= limit:  # 둘이 보트에 같이 탈 수 있으면 start 인덱스 옮겨준다
            start += 1
                
        end -= 1   # end는 항상 보트에 타므로 조건 없이 end 인덱스 옮기기

    return answer

print(solution([70, 50, 80, 50], 100))
