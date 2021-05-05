from collections import deque

priorities = [1, 1, 9, 1, 1, 1]
location = 0
answer = 0

queue = deque([(v, i) for i, v in enumerate(priorities)])

while len(queue):
    printed = queue.popleft()
    if queue and max(queue)[0] > printed[0]:
        queue.append(printed)
    else:

        answer += 1
        if printed[1] == location:
            break

print(answer)
