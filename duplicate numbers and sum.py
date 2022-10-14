def make_final_result(number_list, dup_num_list, new_total):
    #print(number_list, dup_num_list, new_total)
    #print(dup_num_list)
    if (len(dup_num_list) == 0):
        print("no duplicate Number")
    else:

        for i in range(len(dup_num_list)):
            message_text = ", possition  "
            for j in range(len(number_list)):

                if (dup_num_list[i] == int(number_list[j])):
                    k = j + 1
                    message_text = message_text + str(k) + " " + "and "

            print("Duplicate number ", i + 1, " = ", dup_num_list[i],
                  message_text[:-4].rstrip())
        print("sum of the duplicate number = ", new_total)


#s[:-7].rstrip()
try:
    print()
    while True:
        number_list = input("enter the input numbers-->>").split(" ")
        new_number_list = []
        duplicate_number_list = []

        for i in number_list:
            if (i == '-1'):
                break
            else:
                new_number_list.append(i)

        for j in range(len(new_number_list)):
            for k in range(len(new_number_list)):
                if (k != j):
                    if (new_number_list[k] == new_number_list[j]):
                        duplicate_number_list.append(int(new_number_list[k]))
        #duplicate_number_list.sort()
        print(duplicate_number_list)
        total = duplicate_number_list[0]
        new_total = duplicate_number_list[0]
        dup_num_list = [new_total]
        for dup in range(1, len(duplicate_number_list)):
            if (duplicate_number_list[dup] not in dup_num_list):
                total = duplicate_number_list[dup]
                dup_num_list.append(duplicate_number_list[dup])
                new_total = new_total + total

        make_final_result(number_list, dup_num_list, new_total)

except:
    print()
