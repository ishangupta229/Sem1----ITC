n = int(input("Enter the number of rows : \n"))

def pascalsTriangle(n):
  for row in range(1, n+1):
    c = 1
    for i in range(1, row+1):
      print(c, end=" ")
      c = int(c * (row-i)/i)
    #   print("c = ",c , end=",")
    print("")

pascalsTriangle(n)