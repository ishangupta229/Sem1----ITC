import random

i = 1
while i <= 10:
    a = random.randint(0,10)
    b = random.randint(0,10)
    if i == 1:
        print("Can you Answer the following Questions?")
    print("Question" ,i, ":", a ,"*", b , "= \t")
    c = int(input(" "))
    d = a *b
    
    if d == c:
        print("Right!")
    else:
        print("Wrong. The answer is", d)

    i += 1