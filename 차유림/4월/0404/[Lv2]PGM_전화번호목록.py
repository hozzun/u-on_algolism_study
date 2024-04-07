# 해쉬~,,로 풀라고 했는데 잘 모르겟잔아... 근데 실패한 버전이 있는데 아직도 이해가 안가! 
# 정확성 83.3 효율성 16.7
# 근데 예를 들어서 ["119", "97674223", "1195524421"] 이거면 정렬하세요~ 하면 이대로 정렬되야 하는거 아니야 길이순대로????
# 이랬다가 안되서 그냥 sort 했는데 sort는 맞고 길이대로 정렬한건 틀렸어. 왜그래???????

# 왜 why?
# => 예를 들어, ['123', '122', '12344', '1233333'] 이 있으면
# sorted는 => ['122', '123', '123(3)333', '123(4)4'] 로 정렬이 됨. why? 괄호 안의 숫자(문자)처럼 같은 자리의 문자를 더 우선으로 보기 때문~
# but len으로 한다? 그럼 순서가 바뀌겠지요? 

# 헐 이제 봄 대박 ~~~ thx~~~~ 

# -----------실패한 버전 ------------
def solution(phone_book):
    phone_book1 = sorted(phone_book, key = len)
    for i in range(len(phone_book) - 1):
        if phone_book1[i] in phone_book1[i + 1][:len(phone_book1[i])]:
            return False
    return True

# 성공!! 리스트 슬라이싱으로 구해줌 접두어!  
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i + 1][:len(phone_book[i])]:
            return False
    return True
