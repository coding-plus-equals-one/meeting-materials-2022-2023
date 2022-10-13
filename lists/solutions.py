# Challenge 1
def split_gold(golds):
    a = []
    b = []
    for i in range(len(golds)):
        if i % 2 == 0:
            if golds[0] >= golds[-1]:
                a.append(golds[0])
                golds.pop(0)
            else:
                a.append(golds[-1])
                golds.pop(-1)
        else:
            if golds[0] >= golds[-1]:
                b.append(golds[0])
                golds.pop(0)
            else:
                b.append(golds[-1])
                golds.pop(-1)

    return [sum(a), sum(b)]


# Challenge 2
def english_beggars(golds):
    return [sum(golds[::2]), sum(golds[1::2])]


print(english_beggars([1, 2, 3, 4, 5]))
