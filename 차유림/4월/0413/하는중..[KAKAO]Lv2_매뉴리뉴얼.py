# 메뉴 리뉴얼 
# 아직 하는 중 ...... 졸려서 자야겟어.
from itertools import combinations 
# def solution(orders, course):
#     answer = []
#     comb = []
#     for i in course:    
#         for j in orders:
#             comb += list(combinations(j, i))

#     return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
menu = {}
comb = []
for i in course:
    for j in orders:
        comb += list(combinations(sorted(j), i))

for i in comb:
    menu_val = ''.join(i)

    if menu_val in menu:
        menu[menu_val] += 1
    else:
        menu[menu_val] = 1
    
