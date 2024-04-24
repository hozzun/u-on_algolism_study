# 해쉬의 자료구조인 딕셔너리 이용

def solution(clothes):
    answer = 1

    # 딕셔너리에 종류별 의상 개수 세줌
    # ex) 모자: 2개, 안경: 1개
    dict = {}
    for key, val in clothes:
        if val not in dict:
            dict[val] = 1
        else:
            dict[val] += 1

    # 경우의 수로 계산
    # 모자 경우(2개) => 아무것도 쓰지 않을 때, 1번 모자 쓸 때, 2번 모자 쓸 때 [ 총 3번 ]
    # 안경 경우(1개) => 아무것도 쓰지 않을 때, 안경 쓸 때 [ 총 2번 ]
    # 3번 * 2번 = 6번
    # 무조건 1개라도 입으라니까 둘다 아무것도 입지 않는 겹쳐지는거 하나 빼주기
    for count in dict.values():
        answer *= count + 1
        
    return answer - 1
