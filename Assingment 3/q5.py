a = "ABCDEFGHIJK"
b = 0

while len(a)-b*2 >= 1:
    print(" "*b, a[0 : len(a) - b*2])
    b += 1
