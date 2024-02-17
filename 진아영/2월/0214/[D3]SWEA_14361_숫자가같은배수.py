for tc in range(1, 1+int(input())):
    N = input()        # 원본 N
    new_N = list(N)    # 순열 돌려서 비교할 새로운 N
    n = len(N)         # N의 길이
    result = 'impossible'
     
    def perm(i):
 
        global result
 
        # i가 n-1번째 인덱스만큼 다 구했을때 -> 순열 완성!
        if i == n:
            newnew_N = int(''.join(new_N))   # 완성 순열 숫자로 바꾸기
            if newnew_N > int(N) and newnew_N % int(N) == 0:   # 조건에 맞으면
                result = 'possible'  # 결과 possible로 바꿔줌
         
        else:
            for j in range(n):
                new_N[i], new_N[j] = new_N[j], new_N[i]
                perm(i + 1)
                new_N[i], new_N[j] = new_N[j], new_N[i]
 
    perm(0)
    print(f'#{tc} {result}')
