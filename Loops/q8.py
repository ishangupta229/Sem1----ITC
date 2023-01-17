num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
num3 = int(input("Enter 3rd Number : "))
num4 = int(input("Enter 4th Number : "))
num5 = int(input("Enter 5th Number : "))
num6 = int(input("Enter 6th Number : "))
num7 = int(input("Enter 7th Number : "))
num8 = int(input("Enter 8th Number : "))
num9 = int(input("Enter 9th Number : "))
num10 = int(input("Enter 10th Number : "))

list = [ num1 , num2,num3,num4,num5,num6,num7, num8,num9,num10]

p_num = []
n_num = []
even = []
odd = []
occur = []


for a in range (10):
    i = list[a]
    if i >= 0:
        p_num.append(i)
    if i <= 0:
        n_num.append(i)
    if i % 2 == 0 :
        even.append(i)
    if i %2 != 0:
        odd.append(i)
    
      
    
print("positive numbers : " , p_num)
print("positive numbers : " ,n_num)
print("even numbers : " ,even)
print("odd numbers : " ,odd)
# print(occur)

for a in range (10):
    i = list[a]
    x = p_num.count(i)
    y = n_num.count(i)
    z = even.count(i)
    w = odd.count(i)
    print ( i ,"occurs", x+y+z+w, "times")
    



