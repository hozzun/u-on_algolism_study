# 70.8점 ㅎㅋ

def solution(phone_book):
    answer = True
    
    num = []
    for i in phone_book[0]:
        num.append(i)
        
    phone_book.sort()
    for i in range(1, len(phone_book)):
        num_1 = []
        for k in phone_book[i]:
            num_1.append(k)
        for j in range(len(num)):
            if num[j] != num_1[j]:
                if j == 0 :
                    return answer
                break
        else:
            answer = False
            return answer
