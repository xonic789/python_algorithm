def solution(n, lost, reverse):
    answer = n - len(lost)
    for i in range(len(lost)):
        front = reverse[i] - 1
        back = reverse[i] + 1
        if lost[i] == front or lost[i] == back:
            answer += 1
        if answer == n:
            break


    return answer

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))