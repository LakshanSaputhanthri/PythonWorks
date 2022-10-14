try:
    N = int(input("Enter N (size of matrix)"))
    matrix = []

    transpose_matrix = []
    for i in range(N):
        raw = input("enter raw {j}  :".format(j=i + 1)).split(" ")
        for i in raw:
            i = int(i)
        if (len(raw) != N):
            break
        else:
            matrix.append(raw)

    for a in range(len(matrix)):
        trm = []
        for b in range(len(matrix)):
            trm.append(matrix[b][a])
        transpose_matrix.append(trm)

    for k in range(len(matrix)):
        tm = " ".join(transpose_matrix[k])
        print(tm)
except ValueError:
    print("enter an integer numbers")
