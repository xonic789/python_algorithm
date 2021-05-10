

def solution(places):
    answer = [1] * len(places)
    dx1 = [-1, 1, 0, 0]
    dy1 = [0, 0, -1, 1]

    p_cnt = 0

    for i in range(len(places)):
        # 하나의 대기실
        for j in range(len(places[i])):
            # 한줄
            for k in range(len(places[i][j])):
                p_cnt = 0
                if places[i][j][k] == 'O':
                    for l in range(4):
                        nx = j + dx1[l]
                        ny = k + dy1[l]
                        if nx >= len(places[i]) or nx <= -1 or ny >= len(places[i][j]) or ny <= -1:
                            continue
                        if places[i][nx][ny] == 'P':
                            p_cnt += 1
                        if p_cnt >= 2:
                            break
                if p_cnt >= 2:
                    break
                elif places[i][j][k] == 'P':
                    p_cnt = 1
                    for l in range(4):
                        nx = j + dx1[l]
                        ny = k + dy1[l]
                        if nx >= len(places[i]) or nx <= -1 or ny >= len(places[i][j]) or ny <= -1:
                            continue
                        if places[i][nx][ny] == 'P':
                            p_cnt += 1
                        if p_cnt >= 2:
                            break
                    if p_cnt >= 2:
                        break

            if p_cnt >= 2:
                answer[i] = 0
                p_cnt = 0
                break
            else:
                p_cnt = 0


    return answer


print(solution([["POOOP",
                 "OXXOX",
                 "OPXPX",
                 "OOXOX",
                 "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))



# # P 응시자
# # O 빈테이블
# # X 파티션
# answer = []
# # 상하좌우1
# p_cnt = 2
# temp = 0
# cnt = 0
# dx1 = [-1, 1, 0, 0]
# dy1 = [0, 0, -1, 1]
# # 상하좌우2
# dx2 = [-2, 2, 0, 0]
# dy2 = [0, 0, -2, 2]
#
# # 총 대기실
# for i in range(len(places)):
#     # 하나의 대기실
#     for j in range(len(places[i])):
#         # 한줄
#         for k in range(len(places[i][j])):
#             if places[i][j][k] == 'P':
#                 for l in range(4):
#                     nx = j + dx1[l]
#                     ny = k + dy1[l]
#                     if nx >= len(places[i]) or nx <= -1 or ny >= len(places[i][j]) or ny <= -1:
#                         continue
#                     if places[i][nx][ny] == 'O':
#                         nx = j + dx2[l]
#                         ny = k + dy2[l]
#                         if nx >= len(places[i]) or nx <= -1 or ny >= len(places[i][j]) or ny <= -1:
#                             continue
#                         if places[i][nx][ny] == 'P':
#                             temp = 1
#                             break
#                     elif places[i][nx][ny] == 'X':
#                         continue
#                 if temp == 1:
#                     break
#             elif places[i][j][k] == 'O':
#                 cnt = 0
#                 for l in range(4):
#                     nx = j + dx1[l]
#                     ny = k + dy1[l]
#                     if nx >= len(places[i]) or nx <= -1 or ny >= len(places[i][j]) or ny <= -1:
#                         continue
#                     if places[i][nx][ny] == 'P':
#                         cnt += 1
#                     if cnt >= p_cnt:
#                         temp = 1
#                         break
#                 if temp == 1:
#                     break
#     if temp == 1:
#         answer.append(0)
#     else:
#         temp = 0
#         answer.append(1)
#
#         # if k == 'P':
#         #
# return answer