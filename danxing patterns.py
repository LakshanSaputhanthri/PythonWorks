def pairsss(listk, pairs):
    listk = listk
    count = 0
    runtime = len(listk)
    for i in range(len(listk)):
        for j in range(i + 1, len(listk)):
            if (listk[i] == listk[j]):
                listk[j] = "x" * j
                listk[i] = "y" * i
                count = count + 1

    return count


def take_inputs():
    listn = input("Enter the heights :").split()
    listk = []
    for i in range(len(listn)):
        if ((int(listn[i]) > 100) and (int(listn[i]) < 200)):
            listk.append(listn[i])
        else:
            print("plz Enter an positive integers between 100 and 200")
            break
    if (len(listk) > 0):
        return listk


try:

    pairs = 0
    print("Number of dancing pairs ", pairsss(take_inputs(), pairs))
except ValueError:
    print("plz Enter an positive integers between 100 and 200 ")
except TypeError:
    print("plz Enter a list of positive integers between 100 and 200 ")