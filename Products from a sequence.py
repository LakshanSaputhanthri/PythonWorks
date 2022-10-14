def checkcontainzero(n):
    for i in range(len(n)):
        if n[i] == '0':
            print("Enter an integer which does not contain the digit 0")
            return 0


def makeproduct(n):

    numlist = []
    generatenumlist = []
    for i in range(len(n)):
        numlist.append(n[i])

    for j in range(len(n)):
        newnumlist = numlist
        indexval = newnumlist[j]
        newnumlist[j] = "1"
        print(newnumlist)
        product = 1
        for k in range(len(n)):
            product = product * int(newnumlist[k])
        generatenumlist.append(str(product))

        #print(product)
        newnumlist[j] = indexval

    result = ""
    for number in generatenumlist:
        result += number + " "
    #print(result)
    print(" ".join(generatenumlist))


try:
    while True:
        n = input("enter number").strip(" ")
        if (int(n) == -1):
            print("bye")
            break
        if (len(n) < 2 or len(n) > 9):
            print("Plz Enter a Number Between 100 and 100,000,000")
            continue

        else:
            x = checkcontainzero(n)
            if (x == 0):
                break
            else:
                makeproduct(n)

except ValueError:
    print("BYE! /n Plz Enter a Number Between 100 and 100,000,000")
