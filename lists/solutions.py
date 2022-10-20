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


# Challenge 3 Part 1
def josephus_survivor(n, one_every):
    sequ = []
    for i in range(1, n + 1):
        sequ.append(i)
    #print(sequ)
    index = -1
    while len(sequ) != 1:
        index += one_every
        while index >= len(sequ):
            index -= len(sequ)
        #print(sequ[index])
        sequ.pop(index)
        #print(sequ)
        index -= 1
        #print(index)
    return sequ


print(josephus_survivor(7, 3))


# Challenge 3 Part 2
def josephus_permutation(n, k):
    sequ = []
    perm = []
    for i in range(1, n + 1):
        sequ.append(i)
    #print(sequ)
    index = -1
    while len(sequ) != 0:
        index += k
        while index >= len(sequ):
            index -= len(sequ)
        #print(sequ[index])
        perm.append(sequ.pop(index))
        #print(sequ)
        index -= 1
        #print(index)
    return perm


print(josephus_permutation(7, 3))
