from collections import deque
queue = deque()
bridge_length = 2
weight = 10
truck_weights = deque([7, 4, 5, 6])
truck_weight_on_bridge = 0
answer = 0

while len(truck_weights) > 0:
    # 트럭 하나 출발
    if weight >= truck_weight_on_bridge:
        if 
    truck_weight = truck_weights.popleft()
    truck_weight_on_bridge += truck_weight
    answer += 1



    queue.append(truck_weight)

