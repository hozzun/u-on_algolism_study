# 100점
# 첨엔 접근도 못했다가 유림이의 전화번호 목록 문제 훔쳐보고 나서 sort() 숫자로된 문자열 정렬하면 사전순으로 배열된다는걸 알았음!
# 그래서 그 문제 해결하고 나서 이 문제도 그렇게 풀면 될 거 같아서 다시 도전해봄

def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))               # 일단 문자열로 다 바꿔줌
    numbers.sort(key=lambda x:x*4, reverse=True)    # 정렬할 때, 원소의 길이는 최대 4자리니까 최대 문자열 길이만큼 늘린 후 (x*4) 늘려진 문자열을 기준으로 사전식 정렬 해줌
    answer = ''.join(numbers)                       # 그리고 합쳐준다!

    if set(answer) == {'0'}:                        # 이거 안했더니 한문제만 자꾸 틀려서 생각해보니까 모든 원소가 0일 경우에 0000..으로 나옴 그래서 0000인지 확인해줌
        answer = '0'

    return answer
