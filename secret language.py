def secret_code_maker(text):
    secret_code = {
        "a": "a",
        "b": "bob",
        "c": "coc",
        "d": "dod",
        "e": "e",
        "f": "fof",
        "g": "gog",
        "h": "hoh",
        "i": "i",
        "j": "joj",
        "k": "kok",
        "l": "lol",
        "m": "mom",
        "n": "non",
        "o": "o",
        "p": "pop",
        "q": "qoq",
        "r": "ror",
        "s": "sos",
        "t": "tot",
        "u": "u",
        "v": "vov",
        "w": "wow",
        "x": "xox",
        "y": "yoy",
        "z": "zoz",
        "A": "A",
        "B": "Bob",
        "C": "Coc",
        "D": "Dod",
        "E": "E",
        "F": "Fof",
        "G": "Gog",
        "H": "Hoh",
        "I": "I",
        "J": "Joj",
        "K": "Kok",
        "L": "Lol",
        "M": "Mom",
        "N": "Non",
        "O": "O",
        "P": "Pop",
        "Q": "Qoq",
        "R": "Ror",
        "S": "Sos",
        "T": "Tot",
        "U": "U",
        "V": "Vov",
        "W": "Wow",
        "X": "Xox",
        "Y": "Yoy",
        "Z": "Zoz"
    }
    encoder_text = ""
    for i in range(len(text)):
        if ((text[i].isalpha()) and (text[i] in secret_code)):
            encoder_text = encoder_text + secret_code[text[i]]

        elif ((text[i].isalpha()) and (text[i].lower() in secret_code)):
            encoder_text = encoder_text + text[i]
            #encoder_text = encoder_text + secret_code[text[i]]

        else:
            encoder_text = encoder_text + text[i]

    print("Output :", encoder_text)


try:
    while True:
        text = input("input : ")
        secret_code_maker(text)
except:
    print("")