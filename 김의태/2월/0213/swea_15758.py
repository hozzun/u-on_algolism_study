#실패작 원인 모름
# T = int(input())
# for tc in range(1, T+1):
#     s, t = input().split()
#
#     if len(s) >= len(t):
#         short = t
#         long = s
#     else:
#         short = s
#         long = t
#
#     short_len = len(short)
#     long_len = len(long)
#
#     i = 0
#     j = 0
#     while i < long_len:
#         if long[i] == short[j]:
#             i += 1
#             j += 1
#             if j > short_len - 1:
#                 j = j % short_len
#         else:
#             answer = 'no'
#             break
#
#     if i == long_len:
#         answer = 'yes'
#
#     print(f'#{tc} {answer}')

#성공작 but 무식하게 품 이게 아닐텐데?
T = int(input())
for tc in range(1, T+1):
    s, t = input().split()

    if len(s) >= len(t): #길고 짧은거 정하자
        short = t
        long = s
    else:
        short = s
        long = t

    short *= 50 # 만약 short가 1이고 long이 50 인경우 최소 50번은 붙여줘야하므로 걍 50 곱해서 이어붙임
    long *= 50

    if short in long:
        answer = 'yes' # 답 조건
    else:
        answer = 'no'

    print(f'#{tc} {answer}') #출력
