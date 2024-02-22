# 실패

N = int(input())
switch = list(map(int, input().split()))
student = int(input()) # 학생 수

visited = [0] * (N + 1) # 스위치 리스트
for i in range(N):
    visited[i + 1] = switch[i] # 각 스위치 번호(리스트 번호)에 넣어줌

for _ in range(student):
    S, num = map(int, input().split())

    # 남자
    if S == 1:
        for i in range(len(visited)):
            if i % num == 0 and i != 0: # num의 배수면
                if visited[i] == 1:
                    visited[i] = 0
                elif visited[i] == 0:
                    visited[i] = 1

    # 여자
    if S == 2:
        a = 1 # 초기값
        i = num
        while i + a != len(visited):
            if i == 1: # 1번만 있으면 그것만 바꿔줌
                if visited[i] == 0:
                    visited[i] = 1
                    break
                elif visited[i] == 1:
                    visited[i] = 0
                    break

            elif visited[i-a] == visited[i+a]: # 양 좌우가 대칭이면 바꿔줌
                if visited[i-a] == 0 and visited[i+a] == 0:
                    visited[i-a] = 1
                    visited[i+a] = 1

                elif visited[i-a] == 1 and visited[i+a] == 1:
                    visited[i-a] = 0
                    visited[i+a] = 0

            else:
                if visited[i - 1] == visited[i + 1] or visited[i - 1] != visited[i + 1]: # 양옆 다 바꿔주고 자기도 바꿔줌
                    if visited[i] == 0:
                        visited[i] = 1
                        break
                    elif visited[i] == 1:
                        visited[i] = 0
                        break

            a += 1 # 1씩 증가하면서 계속 넓힘

for i in range(1, len(visited)): # 출력
    print(visited[i], end=' ')
    if i % 20 == 0 and i != 0:
        print()
