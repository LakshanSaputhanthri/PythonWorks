from msilib.schema import Error
from multiprocessing.sharedctypes import Value


def makepalindrome(str_num, str_revnum, count):
    x = int(str_num)
    y = int(str_revnum)
    count = count + 1
    number = x + y
    checkpalingdrome(number, count)


def checkpalingdrome(number, count):

    list_acsending1 = []
    list_acsending2 = []
    str_num = str(number)
    str_revnum = str_num[-1::-1]
    length_integer = len(str_num) // 2
    if (len(str_num) % 2 == 0):
        list_acsending1 = list(str_num[0:length_integer])
        list_acsending2 = list(str_num[-1:length_integer - 1:-1])
        list_acsending1.sort()
        list_acsending2.sort()
        if (list_acsending1 == list_acsending2):
            print("palindrome =", number, " number Of addition ", count)
        else:

            makepalindrome(str_num, str_revnum, count)

    else:
        list_acsending1 = list(str_num[:length_integer:])
        list_acsending2 = list(str_num[-1:length_integer:-1])
        list_acsending1.sort()
        list_acsending2.sort()
        if (list_acsending1 == list_acsending2):
            print("palindrome =", number, " number Of addition ", count)
        else:

            makepalindrome(str_num, str_revnum, count)


try:
    while True:
        count = 0
        number = int(input("Enter Input -->> "))
        if (number == -1):
            print("program terminated ")
            break
        checkpalingdrome(number, count)

except:
    print(Error)
