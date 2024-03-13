# 백준 16173번 점프왕 쪨리
# 메모리 31120kb 시간 40ms 코드길이 516B
# 하. 메모리 초과나서 별 짓 다 했는데 0 일때 리턴을 안해줘서 그런거였음
# 아영언니가 어제 이거 풀 때 큰 사실을 놓치고 있었다는게 이거였음..!!!!!!!

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [1, 0] # 오른쪽 아래만 간다 
dj = [0, 1]

result = 'Hing' 

def dfs(r, c):
    global result

    if r == N-1 and c == N-1: # r과 c가 N-1 자리에 가면 (-1 이 라면)
        result = 'HaruHaru' # 하루하루로 result 바꿔줌 
        return 
    
    if arr[r][c] == 0: # 0인 부분이 있다면 바로 리턴해서 힝 출력해줌 
        return 
    
    else:
        jump = arr[r][c] # 자리에 있는 숫자만큼 점프
        for k in range(2):
            nr = r + di[k] * jump 
            nc = c + dj[k] * jump
            if 0 <= nr < N and 0 <= nc < N:
                dfs(nr, nc)
            
dfs(0,0)
print(result)
                    
