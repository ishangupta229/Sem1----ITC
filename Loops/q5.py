# print(chr(65))
# A

num = int(input("Enter the Number of Rows : "))

# a = num//26
# b = num%26

b=65
for  i in range(1,num):
    for j in range(i):
        
        print(chr(b) , end ="") 
        b +=1
        if b==91:
            b = 65

    print("")

# i = 1
# j=1
# b = 65
# while i <= num:
#     while j <=i:        
#         print(chr(b) , end ="")
#         b += 1
#         j +=1 
#         if b==91:
#             b = 65

#     print("")
#     j=0
#     i += 1


