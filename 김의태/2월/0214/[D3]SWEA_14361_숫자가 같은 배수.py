T = int(input())
for tc in range(1, T+1):
    n = input() # digit이 중요하므로 문자열로 입력 받음
    n_list = [num for num in n] # 숫자 하나하나씩 분해
    n_list.sort() # 리스트 정렬해놓기 (편한 비교를 위해)


    n_len = len(n)
    nk_len = len(n)
    k = 2 # 곱해줄 배수
    answer = 'impossible'
    while n_len == nk_len: # 자리수가 다르면 배열은 무조건 어긋나므로 그럴경우 스탑
        nk = str(int(n) * k)
        nk_len = len(nk)
        nk_list = [num for num in nk] #배수만들고 분해하고
        nk_list.sort() #비교를 위해 리스트 정렬

        if nk_list == n_list: #같으면 파서블
            answer = 'possible'
            break
        k += 1

    print(f'#{tc} {answer}')
