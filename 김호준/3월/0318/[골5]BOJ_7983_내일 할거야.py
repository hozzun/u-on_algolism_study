# Python 메모리: 176320KB, 시간: 2360ms, 코드 길이: 285B

import sys # 또 sys안쓰면 시간초과나네..
input = sys.stdin.readline

N = int(input())
arr = []
for tc in range(N):
    d, t = map(int, input().split())
    arr.append((d, t)) # 튜플로 넣음

arr.sort(key=lambda arr:arr[1], reverse=True) # 뒷값 기준으로 내림차순

time = arr[0][1] # 최대 마감기한 설정
for i in range(N):
    time = min(time, arr[i][1]) - arr[i][0]
    # 남은 마감기한에서 과제 숫자 빼면서 계산
    # mim(arr[i]과제의 마감기한과 저장된 남은 기한 중 적은거)

print(time)


# 첨에 재귀 백트래킹으로 풀다가 도저히 return 조건문이 생각안나서 바꿈 
# + 
# 아니 과제를 후다닥 다 해버린다음, 마지막에 쭉 놀면 안되는거임?
# 다하고 노는 걸로 첨에 했다가 틀리길래
# 그냥 최대부터 하나씩 줄이면서 계산해주는걸로 바꿨음
# 놀줄을 모르네; 후딱하고 놀아야지
# + 문제 이거 좀 설명이 부족한거같음 푸는데 스트레스 받음 ㅋ
