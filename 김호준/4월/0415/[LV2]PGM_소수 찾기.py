# 100점

# 순열 사용
from itertools import permutations

# 소수 검열
def prime_check(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return x


def solution(numbers):
    global answer
    # 소수 리스트
    answer = []

    # 1~최대 자릿수까지 순열로 뽑음
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            check = int("".join(j))

            # 중복 수 제거
            if check in answer:
                pass

            # 0과 1은 소수가 아니므로 제거
            elif check == 0 or check == 1:
                pass

            # False면 넘기고, True일 경우, 소수 리스트에 넣기
            else:
                result = prime_check(check)
                if result == False:
                    pass
                else:
                    answer.append(result)

    # 소수의 개수 출력
    return len(answer)
