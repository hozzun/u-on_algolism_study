K = int(input())
'''
우선 나는 처음에 3등분 시켜서 하려고 하다가, 도저히 안될 것 같아서
큰 직사각형에서 빠진걸 빼는 것으로 생각을 바꿔봄

계속 그림 그려보면서 고민하다가 알려주는 순서대로 리스트에 넣고
가장 긴세로 길이 양옆에 가로길이와 가장 긴 가로길이 양옆에꺼로
작은 직사각형 넓이 구할 수 있을거 같아서 시도해봄
'''
all = [] # 전부 리스트
east_west = [] # 동,서 리스트 - 가장 긴 가로길이 뽑는용
south_north = [] # 남, 북 리스트 - 가장 긴 세로길이 뽑는용
for _ in range(6):
    way, side = map(int, input().split())
    all.append(side) # 전부 다넣음
    if way == 1 or way == 2:
        east_west.append(side) # 동,서만 넣음
    elif way == 3 or way == 4:
        south_north.append(side) #남, 북만 넣음

max_h = max(east_west) # 가장 긴 가로길이 뽑기
max_w = max(south_north) # 가장 긴 새로길이 뽑기
h_idx = all.index(max_h) # 전체리스트에서 가장긴 가로길이 인덱스값
w_idx = all.index(max_w) # 가장긴 세로길이 인덱스값

result_h = abs((all[(h_idx-1)%6]) - (all[(h_idx+1)%6]))
result_w = abs((all[(w_idx-1)%6]) - (all[(w_idx+1)%6]))
'''
여기가 이제 문제였는데, 인덱스는 잘 맞췄는데 처음에 음수로 나와서
절대값 붙혀줬었음 그래서 실행해보니 정답도 잘나왔음
but 백준에 시도하니 런타임 에러가 남. OMG
그래서 질문게시판 좀 뒤져봤음.. 이런 vs나 파이참은 리스트 벗어나도
오류없이 출력해주는데, 백준은 아니였음
그래서 %6 을 함으로써 리스트 안벗어나게 하는법을 알아냄
ex) 3%6 하면 3나옴 이런식으로 6안벗어나게함 
'''

result = (max_h * max_w) - (result_h * result_w) # 계산
print(result * K)
