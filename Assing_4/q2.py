num1 = int(input("Enter the Number : "))
r1 = int(input("Range starts from :"))
r2 = int(input("Range ends to :"))


for a in range(r1,r2):
    if num1 % a == 0:
        print( num1, "is divisible by", a)
        