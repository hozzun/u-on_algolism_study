#15758번 무한 문자열 
T = int(input()) 
for tc in range(1, T+1):
    S, T = input().split()
    result = 'yes'
    if S * len(T) == T * len(S): # 6,4 이면 6 * 4 = 4 * 6 같으면 yes 
        print(f"#{tc} {result}")
    else: 
        result = 'no'
        print(f"#{tc} {result}")
