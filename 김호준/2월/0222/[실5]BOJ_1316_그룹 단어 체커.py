# Python 메모리: 31120KB, 시간: 44ms

N = int(input())
result = 0
for tc in range(N):
    word = input() # 단어 넣고
    cnt = '' # 확인용

    if len(word) == 1 or len(word) == 2: # 1, 2글자면 카운트
        result += 1

    else:
        for i in word: # 단어에서 한글자씩 빼서
            if i not in cnt: # 확인용에 없으면 붙여줌
                cnt += i
            elif i in cnt: # 만약 있는데
                if cnt[-1] == i: # 마지막 글자랑 같으면
                    cnt += i # 붙여줌
                elif cnt[-1] != i: # 다르면
                    break # 브레이크
        if word == cnt: # 글자랑 확인용이랑 같으면
            result += 1 # 카운트

print(result)
