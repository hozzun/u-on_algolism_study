# 파이썬     33188 KB, 56 ms
# 파이파이 112364 KB, 168 ms

from heapq import heappop, heappush, heapify

N, M = map(int, input().split()) # 카드수, 반복 횟수
cards = list(map(int, input().split()))
heapify(cards)  # 첨엔 cards = heapify(cards) 이렇게 썼는데 cards = None으로 받아서 오류났음 ! 리턴이 없더라고~

for _ in range(M):
    card1 = heappop(cards)  # 젤 작은 카드 두장 뽑기
    card2 = heappop(cards)

    heappush(cards, card1 + card2)  # 합치기
    heappush(cards, card1 + card2)

print(sum(cards))
