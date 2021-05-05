from itertools import permutations


def solution(numbers):
    answer = ''
    list1 = list(map(''.join, (permutations(numbers, 3))))
    print(list1)
    return answer

solution([6, 10, 2])