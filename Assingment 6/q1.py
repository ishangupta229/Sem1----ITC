
x = int(input("Please enter a number : \n"))



def perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return "It is a perfect number"
    else:
        return "It is not a perfect number"
    
print(perfect_number(x))