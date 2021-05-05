s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s = s[2:-2]
s = s.split('},{')
answer = []
sorted_len_s = sorted(s, key=lambda x: len(x))
for i in sorted_len_s:
    n = i.split(',')
    for j in n:
        if int(j) not in answer:
            answer.append(int(j))
print(answer)
