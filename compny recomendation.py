from ast import Break


def recomended():
    stork_prices = input("Entert stock prices ").split()
    stork_price_list = []
    valued_days = 0
    for i in range(len(stork_prices)):
        stork_price_list.append(float(stork_prices[i]))

    average_price = (sum(stork_price_list) / len(stork_price_list)) + 10

    for j in range(len(stork_price_list)):
        if (stork_price_list[j] > average_price):
            valued_days = valued_days + 1
    if (valued_days >= 3):
        print("Number of Valued Days : ", valued_days)
        print("RECOMENDED")
    else:
        print("Number of Valued Days : ", valued_days)
        print("NOT RECOMENDED")


try:
    recomended()
except ValueError:
    print("Invalid Inputs")
    Break
