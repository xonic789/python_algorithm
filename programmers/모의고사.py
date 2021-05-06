def solution(answers):
    answer = []
    give_up_student1 = [0] * len(answers)
    give_up_student2 = [0] * len(answers)
    give_up_student3 = [0] * len(answers)

    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    student1_n = 0
    student2_n = 0
    student3_n = 0
    for i in range(len(answers)):
        if student1_n == len(student1): student1_n = 0
        if student2_n == len(student2): student2_n = 0
        if student3_n == len(student3): student3_n = 0
        give_up_student1[i] = student1[student1_n]
        give_up_student2[i] = student2[student2_n]
        give_up_student3[i] = student3[student3_n]
        student1_n += 1
        student2_n += 1
        student3_n += 1

    answer = [0] * 3

    for i in range(len(answers)):
        if answers[i] == give_up_student1[i]:
            answer[0] += 1
        if answers[i] == give_up_student2[i]:
            answer[1] += 1
        if answers[i] == give_up_student3[i]:
            answer[2] += 1

    n = max(answer)
    answers = []
    for i in range(len(answer)):
        if answer[i] == n:
            answers.append(i + 1)


    return answers


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))