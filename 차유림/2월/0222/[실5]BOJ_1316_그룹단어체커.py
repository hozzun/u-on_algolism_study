# 백준 1316번 그룹 단어 체커 메모리 31120 kb 시간 44ms
N = int(input())
cnt = N # 그룹단어의 수를 N이라 둔다 
for i in range(N):
    string = input()
    for j in range(len(string) - 1):  
        if string[j] == string[j+1]: # 만약에 j 랑 j+1 이 같으면 
            continue # 계속 반복 
        elif string[j] != string[j+1]: # 만약 안같으면 
            if string[j] in string[j+2:]: # string[j] 가 string[j+2:] 한거에 속한다면 
                cnt -= 1 # 그룹단어가 아니므로 -1 해준다
                break # 그리고 브레이크 걸어서 다음 단어를 확인해준다 

print(cnt)
