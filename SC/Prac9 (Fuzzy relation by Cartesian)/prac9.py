def cartesian():
    n = int(input("\nEnter number of elements in first set (A): "))
    A = []
    B = []
    
    print("Enter elements for A:") 
    for i in range(0, n):
        ele = float(input()) 
        A.append(ele)
    
    m = int(input("\nEnter number of elements in second set (B): ")) 
    print("Enter elements for B:")
    for i in range(0, m): 
        ele = float(input()) 
        B.append(ele)
    
    print("A = {"+str(A)[1:-1]+"}")
    print("B = {"+str(B)[1:-1]+"}")
    
    cart_prod = []
    cart_prod = [[0 for j in range(m)] for i in range(n)] 
    for i in range(n):
        for j in range(m):
            cart_prod[i][j] = min(A[i], B[j]) 
    
    print("A x B = ")
    for i in range(n): 
        for j in range(m):
            print(cart_prod[i][j], end=" ") 
        print("\n")
    
    return cartesian()

cartesian()
