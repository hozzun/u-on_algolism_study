# 40ms 31120kb
# 모듈이 짱이네

from itertools import combinations

l, c = map(int, input().split())

alphs = input().split()

codes = combinations(alphs, l)
all_vowel = ['a', 'e', 'i', 'o', 'u']
alphs = sorted(alphs)

answer = []
for code in codes:
    v_cnt = 0
    for i in code:
        if i in all_vowel:
            v_cnt += 1

    if v_cnt >= 1:
        if l - v_cnt >= 2:
            
            code_list = list(code)
            code_list.sort()
            answer.append(''.join(code_list))

answer.sort()
for ans in answer:
    print(ans)
