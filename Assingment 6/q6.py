def student_data(student_id, student_name=None, student_class=None):
    print('Student ID:', student_id)
    if student_name is not None:
        print('Student Name:', student_name)
    if student_class is not None:
        print('Student Class:', student_class)

i=0
while i == 0:
    x = input("Enter the Student Name : ")
    y = input("Enter the Student Class : ")
    z = input("Enter the Student ID : ")
    student_data(student_id = z, student_name=x, student_class=y)
    print("Do you want to continue")
    a = input(">>> ")
    if a == "Yes" or a == "yes" or a == "y" or a == "Y":
        continue
    else:
        break
