#백준 1759 암호만들기
# 처음에 순열을 사용할까?했는데 중복 제거 안하고 다 나와버림 그래서 조합 사용함 ! 
# permutations가 생각났는데 이 메소드 불러오는거 모르겠어서 이 부분은 찾아봤음,,,!!!! 
# 메모리 31120 kb 시간 48ms 코길 378b

from itertools import combinations
L, C = map(int, input().split())
string = list(map(str, input().split()))
string.sort() # 정렬해줌 ~ 

key = list(combinations(string, L))
vowel = ['a', 'e', 'i', 'o', 'u']

for word in key:
    cnt_vowel = 0
    for i in word:
        if i in vowel:
            cnt_vowel += 1
    
    if cnt_vowel >= 1 and L - cnt_vowel >= 2: # 모음이 1개 이상 자음이 2개 이상이어야 함
        print(''.join(word)) # 문자열 쪼인~
