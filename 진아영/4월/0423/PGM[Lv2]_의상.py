# 96.4점 1번 시간초과... 내일은 여기서 함수를 빼봐야지....

def wear(idx, case):
    global answer, categories, closet

    if idx == len(categories):
        answer += case
        return

    # 현재 인덱스 선택
    wear(idx+1, case * closet[categories[idx]])

    # 현재 인덱스 선택하지 않음
    wear(idx+1, case)

def solution(clothes):
    global answer, categories, closet
    
    answer = -1 # 모두 선택하지 않을 경우 빼줘야하므로 -1로 시작
    closet = {}
    categories = []

    for cloth, category in clothes:
        if category in closet:
            closet[category] += 1
        else:
            closet[category] = 1
            categories.append(category)
        
    wear(0, 1)

    return answer
