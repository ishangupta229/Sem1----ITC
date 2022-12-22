a=list(map(int,input("Enter the numbers separated by space:").split()))

b=[]
for s in a:
    c=(s,s*s)
    b.append(c)

print("\nList containing (n,n^2) is shown below:")
print(b)
