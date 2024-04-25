# 메모리 : 31120kb, 실행시간 : 132ms, 코드길이: 566B

def dfs(idx, sum):
    global max_sum

    if idx == 11:    # 종료조건
        if sum > max_sum:    # 최대값 찾기
            max_sum = sum
        return

    for i in range(11):   # idx 행의 열 순회
        if arr[idx][i] != 0 and visit[i] == 0:   # 방문하지 않았고, 그 값이 0이 아닌경우
            visit[i] = 1
            dfs(idx+1, sum+arr[idx][i])    # sum 누적, 다음 행 dfs호출
            visit[i] = 0

T = int(input())
for tc in range(T):
    arr = [list(map(int, input().split())) for _ in range(11)]
    visit = [0] * 11   # 방문 배열
    max_sum = 0   # 합계 저장할 변수
    dfs(0, 0)    # 0에서 dfs 호출

    print(max_sum)
