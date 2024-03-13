# 파이썬 31120 KB, 44ms, 623 B

N = int(input())  # 전체 사람 수
a, b = map(int, input().split())  # 두사람 사이의 촌수 계산
T = int(input())  # 관계 수
family = [[] for _ in range(N+1)]  # 일촌 관계 정보
visited = [0] * (N+1)

for _ in range(T):
    parent, kid = map(int, input().split())
    family[kid].append(parent)   # 가족 관계 저장
    family[parent].append(kid)

result = -1

def dfs(i, c, time):  # 출발 번호, 찾을 번호, 촌수
    global result

    if i == c:          # 찾아야할 가족에 도달했으면
        result = time   # 촌수 저장해주고
        return          # return

    connection = family[i]   #관련 가족들 뽑아옴

    for j in connection:
        if not visited[j]:   # 그중에 확인 안해본 가족이면
            visited[j] = 1   # 확인표시 해주고
            dfs(j, c, time + 1)    # 그 주변 가족들 다시 확인

    return

dfs(a, b, 0)
print(result)
