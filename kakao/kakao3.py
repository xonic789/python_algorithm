from collections import deque

def solution(n, k, cmd):
    answer = ''
    stack = []
    cmd = deque(cmd)
    chart = ['O'] * n
    while cmd:
        # 커맨드 하나 꺼내기
        command = cmd.popleft()
        # 커맨드가 1보다 클 경우
        if len(command) > 1:
            if command[0] == 'D':
                k += int(command[-1])
            elif command[0] == 'U':
                k -= int(command[-1])
        else:
            if command == 'C':
                stack.append(k)
                chart.pop(k)
                temp = k + 1
                if temp > len(chart) - 1:
                    k -= 1
            elif command == 'Z':
                temp = stack.pop()
                if temp < k:
                    k += 1
                chart.insert(temp, 'O')
    while stack:
        chart.insert(stack.pop(), 'X')

    answer = ''.join(chart)
    return answer


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))