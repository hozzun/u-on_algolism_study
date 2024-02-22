# 메모리 109240 / 시간 108ms

N = int(input())
cnt = N    # 그룹 단어의 개수

for i in range(N):
    word = input()
    arr = []
    for j in range(len(word)):    # 입력 받은 문자열을 배열에 한 자리씩 저장.
        if word[j] not in arr:    # 문자가 중복되지 않은 알파벳이라면 배열에 추가
            arr.append(word[j])
        elif word[j] in arr and arr[j-1] == word[j]:   # 중복이지만 연속된다면 배열에 추가
            arr.append(word[j])
        else:    # 아닌경우, 중복되지만 연속되지 않은 경우 (== 조건에 맞지 않는 경우)
            cnt -= 1    # cnt 감소
            break
print(cnt)
