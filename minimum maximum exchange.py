from re import T


def change_max_and_min(num_list, num_list1):
    num_list1.sort()
    new_num_list2 = num_list
    min_list = num_list1[0:3]
    max_list = num_list1[-1:-4:-1]
    x = []

    #print(num_list1, new_num_list2)
    print(max_list)
    print(min_list)
    print(new_num_list2)
    for i in range(len(new_num_list2)):
        if (new_num_list2[i] == max_list[0]):
            new_num_list2[i] = str(min_list[0])
        elif (new_num_list2[i] == max_list[1]):
            new_num_list2[i] = str(min_list[1])
        if (new_num_list2[i] == max_list[2]):
            new_num_list2[i] = str(min_list[2])
    for j in range(len(new_num_list2)):
        if (new_num_list2[j] == min_list[0]):
            new_num_list2[j] = str(max_list[0])
        elif (new_num_list2[j] == min_list[1]):
            new_num_list2[j] = str(max_list[1])
        if (new_num_list2[j] == min_list[2]):
            new_num_list2[j] = str(max_list[2])
    for k in range(len(new_num_list2)):

        x.append(str(new_num_list2[k]))

    y = " ".join(x)
    print(y)


try:
    while True:
        input_list = input(
            "Enter An Positive Integers include at least 7 numbers and no grater than 50 numbers -->>"
        ).split(" ")
        if (len(input_list) > 7 and len(input_list) < 50):
            num_list = []
            num_list1 = []

            for i in input_list:
                if (i == "-1"):
                    break
                else:
                    num_list.append(int(i))
                    num_list1.append(int(i))

            change_max_and_min(num_list, num_list1)
        else:
            print(
                "<<-- Enter An Positive Integers include at least 7 numbers and no grater than 50 numbers -->> "
            )
            continue

except ValueError:
    print(
        "<<-- Enter An Positive Integers include at least 7 numbers and no grater than 50 numbers -->> "
    )
