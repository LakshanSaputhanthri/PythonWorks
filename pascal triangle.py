while True:
    n = int(input("Enter an Imnteger-->>"))
    if ((n > 0) and (n < 50)):
        pas_trang = [[1, 1]]

        if (n == 1):
            print("   " * n, 1)
        elif (n == 2):
            print("   " * n, 1)
            print("   " * (n - 1), 1, "   ", 1)
        else:

            for i in range(3, n + 1):
                y = []
                for j in range(i):
                    y.append(1)
                pas_trang.append(y)
            #print(pas_trang)
            for k in range(1, len(pas_trang)):
                for m in range(1, len(pas_trang[k]) - 1):

                    pas_trang[k][m] = pas_trang[k - 1][m - 1] + pas_trang[k -
                                                                          1][m]

            pas_trang.insert(0, ["1"])

            for z in range(len(pas_trang)):
                for zz in range(len(pas_trang[z])):
                    pas_trang[z][zz] = "   " + str(pas_trang[z][zz]) + "   "

            for aa in range(len(pas_trang)):
                line = " ".join(pas_trang[aa])
                print("    " * (n - (aa + 1)), line)
                #for bb in range(len(pas_trang[aa])):
