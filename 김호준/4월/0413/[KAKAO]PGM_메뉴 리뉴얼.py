# 100점

from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        # 각 코스별로 조합해서 딕셔너리에 추가 후 카운트
        dict = {}
        for j in orders:
            for menu in combinations(sorted(j), i):
                menu = "".join(menu)
                if menu not in dict:
                    dict[menu] = 1
                elif menu in dict:
                    dict[menu] += 1

        # 예제 3번땜에 조건 넣은 거
        # 만약 dict 비어있으면 pass / 예제 3번이 3글자인데 4개짜리 코스 만들라고 함 에러났음
        if not dict:
            pass
        else:
            max_v = max(dict.values())

        # 만약 value가 최대 값이랑 같고, 2개 이상이면 answer에 추가
        for key, val in dict.items():
            if val == max_v and val >= 2:
                answer.append(key)
    
    # 사전순 정렬
    return sorted(answer)

# 1시간 쫌 안걸린거 같음
# 딱 딕셔너리 쓰면 될거같은 생각이 들어서 품 + 문제에서 힌트를 많이 준듯 ( 조합도 알려주고 )
# key, value 값 꺼내는거 몰라서 구글 쳐밨음 .items() 를 써야하네
# 카카오 별거 아니네 ㅋ
