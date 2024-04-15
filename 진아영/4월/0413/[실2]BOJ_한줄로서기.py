# 31120 KB, 44 ms

N = int(input())
arr = list(map(int, input().split()))    # 처음 인풋
result = [0] * N                         # 결과

for i in range(N):  # 0번 인덱스(1번 사람)부터 돌면서 제자리 찾기
    cnt = 0
    if arr[i] == 0:                      # 만약 i번째 사람의 앞쪽에 i보다 키큰사람이 없으면
        result[result.index(0)] = i+1    # 빈칸 찾아서 그자리 차지하기 (무조건 앞에서부터 차지하기 때문에 index 메서드 사용)
    else:                                # 그렇지 않으면
        for j in range(N):               
            if result[j] == 0:           # 자기보다 키큰사람(빈칸 = 0) 세주기
                cnt += 1
            if arr[i] == cnt:            # 자기보다 키큰사람이 조건에 맞을 경우
                cur = j+1                # j 다음부터 빈칸에 서기 위해 빈칸 찾기
                while True:
                    if result[cur]:      # 빈칸이 아닐경우
                        cur += 1         # 다음칸으로
                    else:                # 빈칸이면
                        break            # 브레이크하고
                result[cur] = i+1        # 그 칸에 들어가기
                break
                
print(*result)
