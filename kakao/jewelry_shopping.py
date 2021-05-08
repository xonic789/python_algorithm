# def solution(gems):
#     answer = []
#     type_len = len(set(gems))
#     gems_len = len(gems)
#     start, end = 0, 0
#     dic = {gems[0]: 1}
#     while start < gems_len and end < gems_len:
#         # dic의 길이가 중복을 제거한 진열대 길이보다 작을 경우
#         if len(dic) < type_len:
#             end += 1
#             if end == gems_len:
#                 break
#
#             dic[gems[end]] = dic.get(gems[end], 0) + 1
#         else:
#             answer.append((end-start, [start + 1, end + 1]))
#             dic[gems[start]] -= 1
#             if dic[gems[start]] == 0:
#                 del dic[gems[start]]
#             start += 1
#     answer = sorted(answer, key=lambda x: x[0])
#
#     return answer[0]

def solution(gems):
    answer = []
    rack_len = len(gems)
    gems_len = len(set(gems))
    start, end = 0, 0
    dic = {gems[start]: 1}
    while start < rack_len and end < rack_len:
        if len(dic) < gems_len:
            end += 1
            if end == rack_len:
                break
            if gems[end] not in dic:
                dic[gems[end]] = 1
            else:
                dic[gems[end]] += 1
        else:
            # answer에 start,end 추가
            answer.append([start + 1, end + 1])
            # start 위치에 있는 키의 벨류를 하나 빼준다.
            # 빼주는 이유는 다음으로 넘어가야 하기 때문에.
            dic[gems[start]] -= 1
            #
            if dic[gems[start]] == 0:
                del dic[gems[start]]
            start += 1
    answer.sort(key=lambda x: (x[1] - x[0]))

    return answer[0]

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
solution(gems)