# 100점

def solution(phone_book):
    dict = {} # 딕셔너리 생성
    for number in phone_book:
        dict[number] = 1 # 1로 저장해줌
    
    for check in phone_book: # 폰넘버 하나씩 뽑아서 ex) '119'
        answer = ''
        for i in check: # 그걸 또 하나씩 연결해보면서 '1', '11', '119'
            answer += i
            
            if answer in dict: # 연결한게 딕셔너리 안에 있으면
                if answer != check: # 대신 본인은 아니여야 함
                    return False # 실패
    
    return True # 무사히 통과하면 성공
