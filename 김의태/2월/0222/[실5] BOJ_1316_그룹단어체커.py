# 31120kb 48ms
# idea : 문자열을 순회하며 글자의 종류를 리스트에 담아 체크하기.
N = int(input())
arr = [input() for _ in range(N)]

answer = 0

for i in range(N): #arr리스트 순회
    str = arr[i]
    str_arr = [str[0]] #문자열의 첫 글자는 미리 넣어둠. 밑에서 인덱스 1번부터 순회하는 코드를 짜서.
    if len(str) >= 2: #문자가 2개 이상인 경우를 따져야하므로
        for x in range(1, len(str)):
            if str[x] not in str_arr: #문자열 하나씩 순회하며 str_arr에 없으면 append
                str_arr.append(str[x])
            else:
                if str[x - 1] != str[x]: #str_arr에 있으며 전 글자와도 다르다? 그럼 답이 아니지
                    break
        else:
            answer += 1 #순회를 다 한 경우는 break 조건에 위배되지 않으므로 정답
    else: # 문자가 하나인경우는 무조건 답
        answer += 1
print(answer)
