try:
    print("")
    while True:
        print("")
        n = int(input("enter an Integer->>"))
        digit_list = []

        if ((n < 50) and (n > 0)):
            for i in range(2, n + 2):
                digit = []
                for j in range(1, i):
                    digit.append(str(j))
                digit_list.append(digit)

            for a in range(1, len(digit_list)):
                digit_list[a] = digit_list[a][-1:0:-1] + digit_list[a]
            for c in range(len(digit_list)):
                x = "     ".join(digit_list[c])
                print(" " * (6 * (n - (c + 1))), x)
        elif (n == -1):
            print("Bye")
            break
        else:
            print("invalid input plz che the input-->>")
            continue

except:
    print("")
