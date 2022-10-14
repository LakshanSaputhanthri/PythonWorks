asci_map = {
    "1": "a",
    "2": "b",
    "3": "c",
    "4": "d",
    "5": "e",
    "6": "f",
    "7": "g",
    "8": "h",
    "9": "i",
    "10": "j",
    "11": "k",
    "12": "l",
    "13": "m",
    "14": "n",
    "15": "o",
    "16": "p",
    "17": "q",
    "18": "r",
    "19": "s",
    "20": "t",
    "21": "u",
    "22": "v",
    "23": "w",
    "24": "x",
    "25": "y",
    "26": "z"
}


def print_code(decode_list):
    decode_list = decode_list
    letters = []
    for i in range(len(decode_list)):
        letter = ""
        for j in range(len(decode_list[i])):
            if (int(decode_list[i][j]) < 26):
                index = str(decode_list[i][j])
                letter = asci_map[index] + letter
        if (len(letter) > 2):
            letters.append(letter[-1::-1])

    print(" ".join(letters))


def asciimapper(number):
    number_list = list(number)
    #print(number_list)
    li = [
        number_list[:], [number_list[0:2], number_list[2], number_list[3]],
        [number_list[0], number_list[1:3], number_list[3]],
        [number_list[0], number_list[1], number_list[2:]]
    ]
    a = li[1][0]
    b = li[2][1]
    c = li[3][2]
    decode_list = [
        number_list[:],
        [str(a[0]) + str(a[1]), number_list[2], number_list[3]],
        [number_list[0], str(b[0]) + str(b[1]), number_list[3]],
        [number_list[0], number_list[1],
         str(c[0]) + str(c[1])]
    ]
    print_code(decode_list)
    #print(len(decode_list))
    #print_code(decode_list)


try:

    while True:
        number = input("Enter 4 Digit Number  -->> ")
        if (len(number) != 4):
            print("Invalid Number Enter 4 Digit Number")
            continue
        else:
            asciimapper(number)
        #print(asci_map["1"])
except:
    print("Invalid Number Enter 4 Digit Number")
