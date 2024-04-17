from collections import deque

def solution(bridge_length, weight, truck_weights):  # 다리에 올라갈수있는 트럭 수, 한계무게, 트럭 무게

    answer = 0
    all_truck = len(truck_weights)        # 지나가야할 트럭 수
    truck_weights = deque(truck_weights)  # 트럭 무게 deque으로 변환
    bridge = deque([0] * bridge_length)   # 다리 queue
    bridge_weight = 0                     # 다리 위 트럭 무게
    pass_truck = 0                        # 지나간 트럭 무게


    while pass_truck < all_truck:   # 트럭이 다 지나갈때까지 반복
      
        # out
        out_t = bridge.popleft()    # 다리위에서 하나 나감
        if out_t != 0:              # 나간게 트럭일경우
            bridge_weight -= out_t  # 나간 무게 빼줌
            pass_truck += 1         # 하나 지나간 표시

        # in
        if truck_weights:                                 # 다리 위에 아직 안올라간 트럭이 있을 경우 올라가도 되는지 조건 확인
            if bridge_weight + truck_weights[0] > weight: # 다음 트럭이 올라올 수 없다면
                bridge.append(0)                          # 그냥 0 올려서 다리 채워준다
            else:                                         # 다음 트럭 올라올 수 있으면
                in_t = truck_weights.popleft()
                bridge_weight += in_t                     # 다리위 무게 늘리고
                bridge.append(in_t)                       # 다리에 트럭 추가

        answer += 1

    return answer

print(solution(2, 10, [7,4,5,6]))
