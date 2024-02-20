# Python 메모리: 31252KB, 시간: 96ms

def f(v): # 함수 만들어보고 싶었음
    for j in range(N):
        if arr[j][0] == v: # 리스트안에 맨 앞 숫자가 K랑 같으면
            find = arr.pop(j) # 따로 뺌
            break # 빠져나가고

    count = 1 # 0등은 없으므로, 1부터
    for i in range(len(arr)):
        if arr[i][1] > find[1]: # 금메달이 K보다 리스트께 더 높으면
            count += 1 # 1증가
        elif arr[i][1] == find[1]: # 금메달 수가 같고
            if arr[i][2] > find[2]: # 은메달이 리스트께 더 높으면
                count += 1 # 1 증가
            elif arr[i][2] == find[2]: # 은메달도 같고
                if arr[i][3] > find[3]: # 동메달이 리스트께 더 높으면
                    count += 1 # 1증가
    return count

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(f(K))
