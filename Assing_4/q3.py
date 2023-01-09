a = int(input("Enter the First side of the triangle"))
b = int(input("Enter the Second side of the triangle"))
c = int(input("Enter the Third side of the triangle"))

s = (a+b+c)/2
print(s)
a = (s*(s-a)*(s-c)*(s-b))**1/2
print("Area =", str(a))

