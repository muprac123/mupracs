def minmax():
    r1 = int(input("Enter number of rows of first relation (R1): "))
    c1 = int(input("Enter number of columns of first relation (R1): "))
    rel1 = [[0 for i in range(c1)] for j in range(r1)]
    print("Enter the elements for R1:")
    for i in range(r1):
        for j in range(c1):
            rel1[i][j] = float(input())

    r2 = int(input("Enter number of rows of second relation (R2): "))
    c2 = int(input("Enter number of columns of second relation (R2): "))
    rel2 = [[0 for i in range(c2)] for j in range(r2)]
    print("Enter the elements for R2:")
    for i in range(r2):
        for j in range(c2):
            rel2[i][j] = float(input())

    print("\nR1 = ")
    for i in range(r1):
        for j in range(c1):
            print(rel1[i][j], end=" ")
        print("\n")

    print("\nR2 = ")
    for i in range(r2):
        for j in range(c2):
            print(rel2[i][j], end=" ")
        print("\n")

    comp = []
    for i in range(r1):
        comp.append([])
        for j in range(c2):
            l = []
            for k in range(r2):
                l.append(min(rel1[i][k], rel2[k][j]))
            comp[i].append(max(l))

    print("\nR1 composition R2 =")
    for i in range(r1):
        for j in range(c2):
            print(comp[i][j], end=" ")
        print("\n")

    return


minmax()
