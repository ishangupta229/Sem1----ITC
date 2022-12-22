x = "Python is a case sensitive language"
l = len(x)
print (l)

#B

b = x[::-1]
print(b)

#C

c = x[10:]
print(c)

#D

d = x[0:10], "object oriented"

#E

for i in range(0,l):
    if x[i] == "a":
        break

print(x[i])
    
#F

for i in range(0,l):
    if x[i] != " ":
        print(x[i])
    