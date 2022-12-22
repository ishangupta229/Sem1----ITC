print("Please enter 3 numbers")
a = int(input("First Number : "))
b = int(input("Second Number : "))
c = int(input("Third Number : "))

if a+b>=c:
    if a+c>=b:
        if c+b>=a:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")






