from itertools import permutations


def demical(number):
    number = int(number)
    if number < 2: return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    numbers = [str(i) for i in numbers]
    temp = []
    for i in range(len(numbers)):
        temp += list(map(''.join, permutations(numbers, i+1)))
    temp = set(temp)
    numbers = [int(i) for i in numbers]
    for i in temp:
        numbers.append(int(i))

    numbers = set(numbers)
    numbers = list(numbers)
    for number in numbers:
        if demical(number):
            answer += 1

    return answer

solution("011")