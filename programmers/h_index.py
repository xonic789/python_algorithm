

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    max_val = citations[0]
    while True:
        cnt = 0
        for b in citations:
            if b >= max_val:
                cnt += 1
        if cnt >= max_val and len(citations) - cnt <= max_val:
            answer = max_val
            break
        max_val -= 1

    return answer




print(solution([3, 0, 6, 1, 5]))

print(solution([2, 3, 5, 4, 9, 10]))