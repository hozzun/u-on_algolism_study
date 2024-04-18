# 21점.....모르겠음..ㅜㅜㅜㅠㅜㅠㅜㅠㅜㅠㅜ푸푸푸ㅠㅜㅠㅜㅠㅜㅜㅠㅡㅜㅡㅜㅠ

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    lst = deque()
    lst = truck_weights
    on_bridge = deque()
    truck = lst.pop(0)
    on_bridge.append(truck)

    while len(lst) != 0 or len(on_bridge) != 0:
        if len(on_bridge) != 0:
            next = on_bridge[0]
        tmp = weight - next  # tmp : 다리에 추가할 수 있는 트럭 무게

        if len(lst) == 0:
            answer += bridge_length + len(on_bridge)
            break

        next = lst.pop(0)  # 다음 트럭 무게 : 추가할지 기다릴지 결정.
        if next > tmp:  # 추가 못하는 경우
            answer += bridge_length + 1  # 통과하기까지 걸리는 시간
            on_bridge = deque()
            on_bridge.append(next)
            # tmp = bridge_length

        else:
            while tmp >= next:  # 무게 제한 내 최대한 들어갈 수 있을 때까지 추가.
                on_bridge.append(next)  # 다리위 트럭 목록에 추가.
                tmp -= next
                if len(lst) > 0:
                    if len(lst) == 1:
                        on_bridge.append(lst.pop(0))
                        answer += bridge_length + len(on_bridge)
                        on_bridge = deque()
                        return answer
                    else:
                        next = lst.pop(0)
                else:
                    break
            answer += bridge_length + 1
            on_bridge = deque()
    return answer
