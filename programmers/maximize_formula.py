from itertools import permutations
import copy


def calc(left_n, right_n, operator):
    left_n = int(left_n)
    right_n = int(right_n)
    if operator == '*':
        return left_n * right_n
    elif operator == '-':
        return left_n - right_n
    else:
        return left_n + right_n


expression = "100-200*300-500+20"
answer = []
per = ['*', '-', '+']
pm = list(map(''.join, permutations(per)))
print(pm)
temp = []
result = []t
lt = 0
for rt in range(len(expression)):
    if expression[rt] == '*' or expression[rt] == '-' or expression[rt] == '+':
        temp.append(expression[lt:rt])
        temp.append(expression[rt])
        lt = rt+1
    if rt == len(expression) - 1:
        temp.append(expression[lt:rt + 1])

for operators in pm:
    compare = copy.deepcopy(temp)
    for operator in operators:
        i = 0
        while i < len(compare):
            if operator == compare[i]:
                result = calc(compare[i - 1], compare[i + 1], compare[i])
                compare[i] = result
                compare.pop(i + 1)
                compare.pop(i - 1)
                i -= 1
            i += 1
    answer.append(abs(compare[0]))
print(max(answer))
