genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
answer = []
genres_total_count = {}
play_genre = {}
for i in range(len(genres)):
    if genres[i] in genres_total_count:
        genres_total_count[genres[i]] += plays[i]
        play_genre[genres[i]] += [(plays[i], i)]
    else:
        genres_total_count[genres[i]] = plays[i]
        play_genre[genres[i]] = [(plays[i], i)]

# 딕셔너리의 아이템을 꺼내면 리스트의 튜플 형태로 나오며, 람다로 x로 받아서
# 키 밸류 형태의 리스트에서 x[1]이란 벨류라는 것이 보장이 되기 때문에
# 리스트의 튜플 형태이므로 for 문에서의 순서 보장이 된다.
# 내림차순 정렬하는 모습이다.
sorted_genres_total_count = sorted(genres_total_count.items(), key=lambda x: x[1], reverse=True)

for genre in sorted_genres_total_count:
    play_list = sorted(play_genre[genre[0]], key=lambda x: x[0], reverse=True)

    for i in range(len(play_list)):
        if i == 2:
            break
        answer.append(play_list[i][1])
print(answer)
