class Employee:

    def __init__(self, age, employment_years, income, department):
        self.age = age
        self.employment_years = employment_years
        self.income = income
        self.department = department

    def getPromotion(self):

        if self.age >= 40:
            new_income = self.income + 1000
            return f"New income is {new_income}"

        elif self.age <= 39:
            return False

        else:
            raise Exception("Unacceptible answer!")

    def changeDepartment(self):
        
        change_department = input("Do you want to change your department: ")
        
        if change_department == "yes":
            new_department = input("In which deparment would you work: ")
            self.department = new_department
            print("Thank you for your answer. We will contact you to discuss this further...")

        elif change_department == "no":
            print("It is nice to hear that you are happy with your woorking place.")

        else:
            raise Exception("Wrong answer!")


