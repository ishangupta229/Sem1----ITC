odd = int(input("Enter an odd number : "))


if odd % 2 == 0 :
    print("Error !!!")
    
else:
    a = int((odd+1)/2)
    for c in range(1,a+1):
        print("*" * c )

    for e in range(a-1, 0 , -1):
        print("*" * e)