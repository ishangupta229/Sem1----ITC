class SumZero:
    def __init__(self,num):
        self.num = num
    def findSumZero(self):
        result = []
        for i in range(len(self.num)):
            for j in range(i+1,len(self.num)):
                for k in range(j+1,len(self.num)):
                    if self.num[i] + self.num[j] + self.num[k] == 0:
                        result.append([self.num[i], self.num[j], self.num[k]])
        return result



num = []
while True:
    x = int(input("Enter the number : "))
    num.append(x)
    a = input("DO you want to enter more number : ")
    if a == "Yes" or a == "yes" or a == "y" or a == "Y":
        print(num)
        continue
    else:
        break
    
sz = SumZero(num)
print(sz.findSumZero())
