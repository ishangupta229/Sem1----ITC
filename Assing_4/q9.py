my_list = []
i=True
while i == True:
    x = input("Enter a word :\n ")
    my_list.append(x)
    y = input("Do you want to enter more names :\n")
    if y == "y" or y == "Y" or y == "YES" or y =="yes":
        i = True
    elif y == "n" or y == "N" or y == "NO" or y =="no":
        i = False
    else:
        break


# print(my_list)
print("")

my_dic = {}

for word in my_list:
    if word in my_dic:  
        b = my_dic[word] 
        b += 1
        my_dic[word]=b
    else:
        my_dic[word]=1

print(my_dic)





    
        




