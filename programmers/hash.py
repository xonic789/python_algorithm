phone_book = ["123","115555","345555","555555", "345444"]
answer = True
phone_book.sort()
for p1, p2 in zip(phone_book, phone_book[1:]):
    if p1 > p2:
        continue
    if p2.startswith(p1):
        answer = False
        break
print(answer)



