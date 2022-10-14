

alphabat = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]


def alphabet_diamand(i):

    diamand_list = alphabat[:i + 1]
    alpa_list = []

    for i in range(len(diamand_list)):
        diamand_str = ""
        for j in range(i + 1):
            diamand_str = diamand_str + str(diamand_list[j])
        alpa_list.append(diamand_str)

    for a in range(len(alpa_list)):
        new_dlist = ["A"]
        newstr = ""

    for b in range(len(alpa_list) - 1):
        newstr = str(diamand_list[(b)]) + newstr

        new_dlist.append(str(alpa_list[b + 1]) + newstr)
    for m in range(len(new_dlist)):
        print(" " * (len(new_dlist) - m) + new_dlist[m])
    zz = 2
    for n in range(len(new_dlist) - 1, 0, -1):

        print(" " * zz + new_dlist[n - 1])
        zz = zz + 1


try:
    while True:
        letter = input("Enter an letter--->>> : ").upper()
        if (len(letter) > 1):
            print("Enter One Letter")
            continue
        if (letter not in alphabat):
            print(" Only One Letter")
            continue
        if (letter in alphabat):
            for i in range(26):
                if (letter == alphabat[i]):
                    alphabet_diamand(i)

except:
    print(Error)
