# 재귀로 했다가 메모리 초과
# def f(x):
#     global N
#     if N == 1:
#         print(*arr, sep='\n')
#         return
#     if N % x == 0:
#         N = N // x
#         arr.append(x)
#         f(x)
#     elif N % x != 0:
#         f(x+1)
# N = int(input())
# arr = []
# f(2)

# Python 메모리: 31252KB, 시간: 2052ms
N = int(input())
arr = []
x = 2
while True:
    if N == 1: # N이 1되면 브레이크
        break
    elif N % x == 0: # x로 나눠 나머지가 0이면
        N = N // x # N은 x로 나눈 몫이 되고
        arr.append(x) # x는 리스트에 추가
    elif N % x != 0: # 나머지가 0이 아니면
        x += 1 # x 1씩 증가
print(*arr, sep='\n')
