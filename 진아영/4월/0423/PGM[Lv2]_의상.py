# 버전2. 함수 빼고 for 문으로 변경~

def solution(clothes):
    global answer, categories, closet
    
    answer = 1
    closet = {}

    for cloth, category in clothes:
        if category in closet:
            closet[category] += 1
        else:
            closet[category] = 1
            
    cnts = closet.values()
    
    for cnt in cnts:
        answer *= (cnt + 1)   # 안입는경우 ~ 옷고르는 경우까지 모든 경우의 수 곱한다

    return answer - 1

#-------------------------------------------------------------------------

# 버전1. 96.4점 1번 시간초과... 내일은 여기서 함수를 빼봐야지....

def wear(idx, case):
    global answer, categories, closet

    if idx == len(categories):
        answer += case
        return

    # 현재 인덱스 중 하나 골라서 입는 경우의 수 곱해서 넘김
    wear(idx+1, case * closet[categories[idx]])

    # 현재 인덱스 안입는경우
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
