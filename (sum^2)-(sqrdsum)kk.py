def squreOfSomefn(number):
    total = 0
    squreOfSome = 0
    for i in range(number + 1):
        total = total + i
    squreOfSome = total**2
    return squreOfSome


def someOfSqurefn(number):
    sumOfSqure = 0
    while (number > 0):
        sumOfSqure = sumOfSqure + number**2
        number = number - 1
    return sumOfSqure


try:
    while True:
        number = int(input("enter a Number : "))
        if (number == -1):
            print("BYE!")
            break
        print(squreOfSomefn(number) - someOfSqurefn(number))

except ValueError:
    print("Enter a Integer Number")
except NameError:
    print("Check the value")
