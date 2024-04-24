# BOJ 3980 / Python, 메모리: 31120KB, 시간: 132ms, 코드 길이: 470B

def recur(cnt, total):
    global answer
    # 11명 되면 최대 값 갱신
    if cnt == 11:
        answer = max(answer, total)
        # 11명 찍고 리턴하면서 백트래킹으로 다른 값들도 돌아보자
        return
    
    # 각 인덱스 다 돌면서 11명 맞춰줌
    for i in range(11):
        # 선수의 값이 있고, 방문 안했다면 11명 채울 때 까지 진행
        if arr[cnt][i] and not visited[i]:
            visited[i] = True
            recur(cnt + 1, total + arr[cnt][i])
            # 백트래킹으로 전부 다 돌아보자
            visited[i] = False


T = int(input())
for tc in range(1, T+1):
    answer = 0
    
    # 방문 처리
    visited = [False] * 11
    # 선수 목록
    arr = [list(map(int, input().split())) for _ in range(11)]

    recur(0, 0)
    print(answer)
