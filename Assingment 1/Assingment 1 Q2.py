gross_income = int(input("Please enter your income : "))
standard_deduction = 10000
dependent_deduction = 3000
number_of_dependents = int(input("Please enter number of dependents : "))


taxable_income = gross_income - standard_deduction - (dependent_deduction * number_of_dependents)
tax_rate = 0.20
tax = taxable_income * tax_rate
print(taxable_income)
print("Your Total Tax Amount is : " + str(tax))