# 하드코딩함.. 어떻게 깔끔하게 뽑지?

from itertools import combinations

def solution(orders, course):
    answer = []
    
    menu_cnt = {}     # 메뉴 카운트 딕셔너리
    menu_list = set() # 메뉴 셋
    
    # 들어온 메뉴 정리
    for order in orders:
        for i in range(2, len(order)+1):        # 메뉴 조합 경우의 수 (2개부터 쭉 뽑기~)
            lst = list(combinations(order, i))

            for j in lst:                 # 그 조합을 하나씩 보면서
                j = list(j)
                j.sort()                  # 근데 순서대로 넣어야하니까 정렬해줘야함
                elem = ''.join(j)
                menu_list.add(elem)       # 메뉴 셋에 추가해주고 (중복 없애려고 셋에 추가)
                if elem in menu_cnt:      # 메뉴 딕셔너리에도 추가해서 몇갠지 세줌
                    menu_cnt[elem] += 1
                else:
                    menu_cnt[elem] = 1
    
    # 이제 course 돌면서 메뉴 갯수별 최대 주문수 정해주기
    for c in course:
        max_course = 0
        max_course_menu = []  # 최대 주문수가 같으면 둘다 뽑아야 하므로 리스트로 받아줌

        for menu in list(menu_list):   # 나온 메뉴중에서 하나를 뽑아서
            if len(menu) == c and menu_cnt[menu] == max_course:   # 그 메뉴 길이가 c와 같고, 주문수가 지금까지의 최댓값이랑 같으면
                max_course_menu.append(menu)                      # 후보에 append
            elif len(menu) == c and menu_cnt[menu] > max_course and menu_cnt[menu] >= 2:  # 메뉴 길이가 c와 같고, 최댓값보다 크면
                max_course = menu_cnt[menu]                                               # 새로 갱신
                max_course_menu = [menu]

        answer.extend(max_course_menu)  # 결과 answer에 추가
                
    answer.sort()
    return answer
