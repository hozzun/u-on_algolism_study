# 100점

def solution(phone_book):
    answer = True

    phone_book.sort()  # 문자열 사전순 정렬
                        -> 유림이가 전화번호 목록 쉽대서 도대체 뭐가 쉽다는거지!? 해서 훔쳐봤는데
                           sort 문자열로 구성된 리스트에 쓰면 사전순 정렬 되는거 첨 알았음!!! thx~;)
    
    for p in range(len(phone_book)-1):                               # 순서대로 하나 뽑아서
        if phone_book[p] == phone_book[p+1][:len(phone_book[p])]:    # 그 다음 순서의 글자의 길이만큼 같은지 확인
            answer = False
          
    return answer
