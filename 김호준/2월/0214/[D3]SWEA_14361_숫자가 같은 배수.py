'''
처음에 곱한거 리스트에 싹다 넣고 N을 for문으로 하나씩 뽑아서 리스트값 하나하나 돌면서
그 안에 있으면 possible 했는데 생각해보니 예를들어 1035면 10350도 맞다고 뜸 그래서 계속
몇십개만 맞다고 떠서, 계속 생각해보다 저게 잘못되었다고 깨달아서 다시 품 어렵다 ;;
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 값 넣고
    result = 0 # 초기값 설정 / 최대한 리스트 안쓰고 싶었음
    for i in range(2, 10): # 범위 최대한 줄이고 싶은데 모르겠음 (2, 8~9) 하니까 103개만 맞음 ㅋㅋ
        result = N * i # 1은 똑같으니까 2부터 넣어줌
        if len(str(N)) == 1 or len(str(result)) == 1: # 한자리수면 브레이크 버림
            # 길이수 재려고 문자열로 변경
            break
        else:
            a = sorted(str(N)) # 문자열로 변경해서 정렬해줌(문자열 아니면 정렬안됨)
            b = sorted(str(result)) # 여기도 정렬해줌
            if str(a) == str(b): # 만약 정렬했는데 둘이 똑같다면
                result = 1 # 1로 바꿔주고 브레이크
                break
    if result == 1: # 만약 1이면 possible 출력
        print(f'#{tc} possible')
    else: # 아니면 impossible
        print(f'#{tc} impossible')
