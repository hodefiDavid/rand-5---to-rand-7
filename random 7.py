import random
import numpy as np


def mat(row, col):
    return np.zeros((row, col))


def percentage(part, whole):
    return 100 * float(part) / float(whole)


random.seed(1)


# the problem is to make a random function (rand 7, however I did it for any given number)
# with only function that return random of 5
# (in this code I used random.randint(1, 5))
# this function get a start and end and will return
def rnd(start=0, end=10):
    sum = 0
    for j in range(end - start):
        sum += random.randint(1, 5)

    ans = sum % (end - start) + 1
    return ans


# Algo2 using mat
def rnd2():
    m = mat(5, 5)
    ar = [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]
    for i in range(5):
        for j in range(5):
            m[i][j] = ar.pop(random.randint(0, len(ar) - 1))

        x = random.randint(0, 4)
        y = random.randint(0, 4)
        while m[x][y] == 0:
            x = random.randint(0, 4)
            y = random.randint(0, 4)
        return m[x][y]

### TEST ###
# making a random for each given num by rand5
# for checking purpose
precision = 100000
for i in range(10, 50, 10):
    arrCh = np.zeros(i + 1)
    arrChMy = np.zeros(i + 1)
    for j in range(precision):
        arrChMy[rnd(end=i)] += 1
        arrCh[random.randint(1, i)] += 1

    spused_prcent = 100 / i
    print("\n\n\n NNN -  result for the num ", i, " supposed percent :", spused_prcent)
    maxDiff = 0
    for r in range(1, i + 1):
        print(r, " - ", arrCh[r], "that is ", percentage(arrCh[r], precision), " percent")
        absu = abs(percentage(arrCh[r], precision) - spused_prcent)
        if absu > maxDiff:
            maxDiff = absu
    print("the biggest distance was ", maxDiff, " percent")

    maxDiff = 0
    print("\n\n\n MMM - result for the num ", i, " supposed percent :", spused_prcent)
    for r in range(1, i + 1):
        print(r, " - ", arrChMy[r], "that is ", percentage(arrChMy[r], precision), " percent")
        absu = abs(percentage(arrChMy[r], precision) - spused_prcent)
        if absu > maxDiff:
            maxDiff = absu
    print("the biggest distance was ", maxDiff, " percent")
