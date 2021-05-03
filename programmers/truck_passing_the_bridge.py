from collections import deque
truck_on_bridge = deque()
complete = deque()
bridge_length = 100
weight = 100
truck_weights = deque([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
truck_length = len(truck_weights)
truck_weight_on_bridge = 0
answer = 0

while len(complete) < truck_length:
    # 트럭 하나 출발

    for i in range(bridge_length):
        # 길이만큼 포문 작동
        # 시간 추가
        # 무게 확인
        try:
            temp = truck_weights[0]
        except IndexError:
            pass
        if weight >= truck_weight_on_bridge + temp:
            truck = truck_weights.popleft()
            truck_weight_on_bridge += truck
            truck_on_bridge.append(truck)
        answer += 1
    if len(truck_on_bridge) != 0:
        complete_truck = truck_on_bridge.popleft()
        truck_weight_on_bridge -= complete_truck
        complete.append(complete_truck)



