try:
    while True:
        char = [
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
            "z"
        ]

        letter = list(input("Enter a letter  -->>").strip())
        if (letter[0] == "0"):
            break

        for i in range(len(letter)):
            if (letter[i] in char):
                #print(list(letter))
                accendin_list = []
                decsendind_list = []
                length = len(letter) // 2
                if (len(letter) % 2 == 0):
                    accendin_list = letter[0:length:1]
                    decsendind_list = letter[-1:length - 1:-1]
                else:
                    accendin_list = letter[0:length:1]
                    ecsendind_list = letter[-1:length:-1]
                accendin_list.sort()
                decsendind_list.sort()
            else:

                1 / 0

        if (accendin_list == decsendind_list):
            print("yes")
        else:
            print("NO")
except NameError:
    print("Enter a letters ")
except ZeroDivisionError:
    print("Enter a letters ")
