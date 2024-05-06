# 6시간초과 후 7트만에 성공 ...
# 질문게시판 좀 훔쳐봤음 ㅎ.ㅎ

# BOJ 14889 / Python, 메모리: 31120KB, 시간: 5300ms, 코드 길이: 728B
import sys
input = sys.stdin.readline

def recur(cnt, idx):
    global answer
    
    # 선수들이 반반 나눠졌다면
    if cnt == N//2:
        start = 0
        link = 0

        for i in range(N):
            for j in range(N):
                # start 팀
                if visited[i] and visited[j]:
                    start += S[i][j]
                    
                # link 팀
                elif not visited[i] and not visited[j]:
                    link += S[i][j]
        
        # 둘의 차이 최소 값 저장
        answer = min(answer, abs(start-link))

    else:
        # 여기서 처음에 N만 해줬다가 시간초과 뜸
        # 어차피 방문 했던 인덱스는 안돌아도 되서 그거 제외 처리로 idx부터 시작 
        for i in range(idx, N):
            # 방문안했으면, 백트래킹하면서 선수맞춰줌
            if not visited[i]:
                visited[i] = True
                # 여기서도 처음에 idx + 1로 했는데, 시간초과 나더라..
                recur(cnt + 1, i)
                visited[i] = False


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N

answer = 1e9
recur(0, 0)
print(answer)

#-------------------------------------------------------------------------------

# 시간초과 ver.
def recur(cnt):
    global answer

    if cnt == N//2:
        start = 0
        link = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += S[i][j]
                elif not visited[i] and not visited[j]:
                    link += S[i][j]

        answer = min(answer, abs(start-link))
        return

    else:
        # 여기 때문에 시간초과
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                recur(cnt + 1)
                visited[i] = False


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N

answer = 1e9
recur(0)
print(answer)
