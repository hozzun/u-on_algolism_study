T = int(input())
for tc in range(1, T+1):
    S, T = input().split()

    arr1 = S * len(T) # 길이수 서로 같게하기 위해 서로의 길이 곱해줌
    arr2 = T * len(S)

    if arr1 == arr2: # 같으면 출력
        print(f'#{tc} yes')
    else:
        print(f'#{tc} no')
