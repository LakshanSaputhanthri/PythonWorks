try:
    while True:

        sequence_list = input("Enter Sequence List Sn -->>").split(" ")
        sequence_list_int = []
        sn1 = []
        sn2 = []
        based = int(input("Enter an based Integer "))
        if (len(sequence_list) > 1 and len(sequence_list) < 100):
            if ((based > 1) and (based < len(sequence_list))):
                for i in sequence_list:
                    if (i == '-1'):
                        break
                    else:
                        sequence_list_int.append(int(i))

                for j in range(len(sequence_list_int)):
                    if (sequence_list_int[j] > int(
                            sequence_list_int[based - 1])):
                        sn2.append(sequence_list[j])
                    else:
                        sn1.append(sequence_list[j])

                b = " ".join(sn1)
                c = " ".join(sn2)
                print("partition sn1 :", b)
                print("partition sn2 :", c)
            if ('-1' in sequence_list):
                break
        else:
            print(
                "Enter the sequense include between 10 and 100 positive integers"
            )
except ValueError:
    print("enter an Integer")
