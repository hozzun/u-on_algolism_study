# 메뉴 리뉴얼 
#orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
#course = [2, 3, 4]

from itertools import combinations # 조합구하기

def solution(orders, course):
    menu = {} # 메뉴 딕셔너리 만들어줄거
    comb = [] # 조합 리스트 만들어서 담을거 
    for i in course:
        for j in orders:
            comb += list(combinations(sorted(j), i)) # 정렬해서 조합 만들어준다! 

    for i in comb: # 조합리스트에서 하나씩 뽑아가지고 
        menu_val = ''.join(i) # 문자열 합쳐준다음에 메뉴 딕셔너리 만들거임!! 

        if menu_val in menu: # 메뉴 딕셔너리에 이미 있는 값이면 1 증가시켜주고 
            menu[menu_val] += 1
        else:
            menu[menu_val] = 1 # 없는 값이면 1로 해서 만들어줌 


    # 가장 많이 등장하는 값을 찾아야 함 길이마다 최댓값 딕셔너리 만들어줌 ex. {2:4, 3:3, 4:2}
    max_cnt = {}
    for i in course:
        max_c = 0
        for key, value in menu.items():
            if len(key) == i and value > max_c:
                max_c = value
        max_cnt[i] = max_c

    result = [] 
    for key, value in menu.items():
        if value == max_cnt[len(key)] and value >= 2: # value 가 max_cnt[len(key)] 와 같고 2 이상일때 
            # key의 길이가 2라고 하면 max_cnt[2] 는 4이고 value 가 4인 것을 찾아야함 
            result.append(key) # result 에 넣어줌

    result.sort() # 정렬

    return result
