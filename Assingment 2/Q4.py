a = int(input("Enter First Number : "))
b = int(input("Enter SEcond Number : "))
c = int(input("Enter Third Number : "))

if a>=b and a>=c:
    print(str(a) + " is the greatest number")
elif b>=a and b>=c:
    print(str(b) + " is the greatest number")
elif c>=a and c>=b:
    print(str(c) + " is the greatest number")