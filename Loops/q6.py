r1 = int(input("Enter Start of range : \n"))
r2 = int(input("Enter End of range : \n"))
bool= True
for a in range(r1,r2+1):
    bool= True
    for j in range(2,a):
        if a % j == 0:
            bool = False
            break
    if bool:
        print( a , end=" ")
        