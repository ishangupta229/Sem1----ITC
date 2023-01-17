s = input("Enter a string : ")

i = len(s)
a = 1
b=""
# print(i)
while a <=i :
    q = s[-a]
    b += q
    a += 1
    # print(b)

print(b)
