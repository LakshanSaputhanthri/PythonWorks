def make_factor(n):
    n_2 = n * 2
    total = 0
    factors = []
    for i in range(n):
        if (n % (i + 1) == 0):
            factors.append(i + 1)
            total = total + (i + 1)
    if (total == n_2):
        print(n, "is perfect")
    elif (total > n_2):
        deference = total - n_2
        print(n, "is abundant by", deference)

    else:
        deference = n_2 - total
        print(n, "is deficient by", deference)


try:

    while True:
        n = int(input("Enter an Integer : "))
        make_factor(n)
except ValueError:
    print("Ente an integer")
