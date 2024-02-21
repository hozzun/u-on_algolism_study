# 메모리: 45,060KB, 시간: 98ms

T = int(input())
for tc in range(1, T+1):
    arr = input() # 입력

    for i in range(1, 30):
        if arr[0:i] == arr[i+1:i+i+1]: # 슬라이싱으로 계산하여 뒤에꺼랑 같아지면
            print(f'#{tc}', len(arr[0:i+1])) # 길이 출력
            break # 브레이크
