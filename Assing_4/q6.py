r1 = int(input("Enter Start of range : \n"))
r2 = int(input("Enter End of range : \n"))

for a in range(r1,r2+1):
    for j in range(2,a):
        if a % j == 0:
            break
    else:
        print( a , end=" ")
        