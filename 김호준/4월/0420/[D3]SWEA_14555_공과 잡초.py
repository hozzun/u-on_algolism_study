# SWEA 14555 / 메모리: 43,976KB, 실행시간: 112ms, 코드길이: 186

T = int(input())
for tc in range(1, T+1):
    S = input()

    count = 0

    count += S.count('()')
    count += S.count('|)')
    count += S.count('(|')

    print(f'#{tc}', count)


# 아니 이게 왜 맞아? ㅋㅋ 걍해본건데
# 첨에 초원에 놓는건줄 알았는데
# 문제보니까 "초원에 놓였을 수 있는" 이라고 되어있길래 잡초랑 묶어서 했는데 답나오길래
# 제출하니까 맞음.. 이거 맞음? 어이가 없어서 헛웃음 나옴
