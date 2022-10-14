def expansion(digitlist):
    digit_list = list(digitlist)
    #print(digit_list)
    result_list = []
    x = 0
    for i in digit_list[-1::-1]:

        #print(str(i) + "*" + "2^" + str(x))
        resultExpan = str(i) + "*" + "2^" + str(x)
        result_list.append(resultExpan)
        x = x + 1
    return (" + ".join(result_list))


try:
    while True:
        int_number = int(input("Enter an Integer between 1 and 10,000  :->>"))
        if (int_number == 0):
            print("Program Terminated")
            break
        elif (int_number > 10000 or int_number < 1):
            print("Enter an Integer between 1 and 10,000")
        else:
            boolnumber = str(bin(int_number))
            print(boolnumber[2:], " = ", expansion(boolnumber[2:]))

except:
    print("something went wrong")
#print(list(bin(x)))