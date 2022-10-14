def define_anagrams(first_string_list, second_string_list):
    first_string_list = first_string_list
    second_string_list = second_string_list
    first_string_list.sort()
    second_string_list.sort()
    first_string = ""
    second_string = ""
    for i in range(len(first_string_list)):
        first_string = first_string + first_string_list[i]
    for j in range(len(second_string_list)):
        second_string = second_string + second_string_list[j]

    if (first_string.lower() == second_string.lower()):
        print("anagrams")
    else:
        print("There are not anagrams")


def take_an_strings():
    string_1 = input("Enter string One --> ")
    string_2 = input("Enter string Two --> ")
    first_string_list = []
    second_string_list = []
    for i in string_1:
        if (i.isalpha()):
            first_string_list.append(i)
        elif (i == " "):
            continue
        else:
            5 / 0

    for j in string_2:
        if (j.isalpha()):
            second_string_list.append(j)
        elif (j == " "):
            continue
        else:
            5 / 0

    define_anagrams(first_string_list, second_string_list)


try:

    take_an_strings()
except ZeroDivisionError:
    print("plz enter only an alphebetic charactors")
