try:

    def diagonal_matrix(matrix):
        mat = matrix
        upper = []
        lower = []

        for i in range(len(mat) - 1):
            for j in range(i + 1, len(mat)):
                upper.append(int(mat[i][j]))

        for k in range(-1, len(mat)):
            for l in range(0, k):
                lower.append(int(mat[k][l]))

        upt = 0
        lowt = 0

        for z in range(len(upper)):
            upt = upt + upper[z]
            lowt = lowt + lower[z]
        if ((upt == 0) and (lowt == 0)):
            print("3")
        elif (upt == 0):
            print("2")
        elif (lowt == 0):
            print("1")
        else:
            print("4")

    N = int(input("Enter N (size of matrix)"))
    matrix = []
    if (N <= 8):

        all_raw = []

        for i in range(N):
            raw = input("enter raw {j}  :".format(j=i + 1)).split(" ")
            for i in raw:
                i = int(i)
            if (len(raw) != N):
                break
            else:
                matrix.append(raw)
        diagonal_matrix(matrix)
    else:
        print("plz check the input length")
except:
    print("Enter an Integer")