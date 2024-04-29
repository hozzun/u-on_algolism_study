# BOJ 15093 카드 합체 놀이 / Python, 메모리: 31120KB, 시간: 160ms, 코드 길이: 268B

N, M = map(int, input().split())
arr = list(map(int, input().split()))

i = 0
while True:
    # 매번 오름차순
    arr.sort()

    # M번 채워지면 종료
    if i == M:
        break

    # 낮은 카드 2개 뽑아줌
    a = arr.pop(0)
    b = arr.pop(0)

    # 2개를 합해주고 다시 넣어줌
    c = a + b
    arr.append(c)
    arr.append(c)

    # M번까지 카운트
    i += 1

# 종료되면 카드의 합 출력
answer = sum(arr)
print(answer)

# 덱으로 할랬는데.. 덱으로하니까 왜 while문에서 sort가 안되지..?
