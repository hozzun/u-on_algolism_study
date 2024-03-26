# 파이썬    31120 KB, 48 ms, 721 B
# 파이파이 111328 KB, 128 ms


L, C = map(int, input().split())   # 암호 길이, 문자열 수
char = list(input().split())
char.sort()   # 정렬
require_char = ['a', 'e', 'i', 'o', 'u']   # 헤엑 cstw가 왜 안되지? 한참 생각하고보니 이런 조건이 있엇음

def make(idx, word, i):

    # 단어 다 모았을때, 조건 확인
    if len(word) == L:
        rec = non_rec = 0   # 모음수, 자음수
      
        for j in word:      # 모음, 자음 세기
            if j in require_char:
                rec += 1
            else:
                non_rec += 1
              
        if rec >= 1 and non_rec >= 2:   # 암호 조건
            print(word)
          
        return
    
    if idx >= C:
        return
    
    
    # 해당 인덱스 선택
    make(idx + 1, word + char[idx], i + 1)
    
    # 해당 인덱스 미선택
    make(idx + 1, word, i)


make(0, '', 0)
