# swea 2007번 패턴 마디의 길이 
# 메모리 43248 kb 시간 111ms

T = int(input())
for tc in range(1, T+1):
    string = input()
    pattern = '' # 패턴변수에 마디 문자열 넣어줄것임
    for i in range(1, 11): # 마디의 최대 길이는 10 
        if string[:i] == string[i:i*2]: #  'KOREA' == 'KOREA' 라면 
            pattern = string[:i] # 패턴에 앞에꺼 넣어줌 
            break # 아ㅏ~~~~~~놔 브레이크 안해서 계속 7개만 맞음 ㅡㅡ^

    print(f"#{tc} {len(pattern)}") # 패턴의 길이 프린트
