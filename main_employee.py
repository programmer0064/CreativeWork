from employee import Employee

employee1 = Employee(age=int(input("What is the age of the employee: ")), employment_years=int(input("How many years have you worked with us: ")), income=int(input("What is the income of the employee: ")), department=input("What is the department of the employee: "))
result = employee1.getPromotion()
print(result)
employee1.changeDepartment()