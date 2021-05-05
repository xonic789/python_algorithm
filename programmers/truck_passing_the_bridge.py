from collections import deque
bridge_length = 100
truck_on_bridge = deque([0] * bridge_length)
weight = 100
truck_weights = deque([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
truck_length = len(truck_weights)
truck_weight_on_bridge = 0
answer = 0

while truck_weights:
    # 시간 증가
    answer += 1
    bridge_out = truck_on_bridge.popleft()
    truck_weight_on_bridge -= bridge_out

    if weight < truck_weights[0] + truck_weight_on_bridge:
        truck_on_bridge.append(0)
    else:
        truck = truck_weights.popleft()
        truck_on_bridge.append(truck)
        truck_weight_on_bridge += truck

while truck_weight_on_bridge > 0:
    answer += 1
    bridge_out = truck_on_bridge.popleft()
    truck_weight_on_bridge -= bridge_out

print(answer)

