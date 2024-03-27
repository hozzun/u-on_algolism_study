# Python 메모리: 31120KB, 시간: 40ms, 코드 길이: 436B

from itertools import combinations # 조합

L, C = map(int, input().split())
arr = list(map(str, input().split()))
mo_arr = ['a', 'e', 'i', 'o', 'u'] # 모음 리스트

alpha = [] # 사전순 L자릿수의 조합 리스트
for i in combinations(sorted(arr), L):
    alpha.append(''.join(i)) # 'a', 'b' 이렇게 되어있길래 join으로 뭉쳐줌

for i in range(len(alpha)): # 모든 L자릿수의 조합 알파벳들을
    mo = 0 # 모음 개수
    ja = 0 # 자음 개수
    for j in range(L): # 0~L자릿수 별로 뽑아 내면서
        if alpha[i][j] in mo_arr: # 모음이면
            mo += 1 # 모음 수 증가
        else: # 자음이면
            ja += 1 # 자음 수 증가

    if mo >= 1 and ja >= 2: # 최소조건 모음 1개 이상, 자음 2개이상이 되면
        print(alpha[i]) # 출력
