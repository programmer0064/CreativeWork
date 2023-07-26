students_class = ["Berk Akbulut", "Beren Akbulut", "Hava Akbulut", "Özgür Akbulut"]

for i in students_class:
    print(i)

def addOnlyOneStudent(students):
    while True:
        add_student = input("Do you want to add a student? yes/no ")
        
        if add_student == "yes":
            
            add_students = input("Do you want to add more than one student? yes/no ")
            
            if add_students == "yes":
                number_of_students = int(input("How many students do you wnat to add? "))

                for i in range(number_of_students):
                    name = input(f"Give me the name of the {i+1}.student: ")
                    students.append(name)
                break

            elif add_students =="no":
                add_name = input("What is the name of the student? ")
                students.append(add_name)
                break

            else:
                print("Wrong type of answer!")
        
        elif add_student == "no":
            print("Alright! Thanks for the answer.")
            break
        
        else:
            print("Your answer to the question is inappropriate!")

def deleteOnlyOneStudent(students):
    while True:
        delete_student = input("Do you want to delete a student? yes/no ")

        if delete_student == "yes":

            delete_students = input("Do you want to delete more than one student? yes/no ")

            if delete_students == "yes":

                number_delete = int(input("How many students do you want to delete? "))

                for i in range(number_delete):
                    name= input(f"What is the name of the {i+1}.student? ")
                    students.remove(name)
                break

            elif delete_students == "no":
                name = input("What is the name of the student you want to delete? ")
                students.remove(name)
                break

            else:
                print("Unappropriate answer")

        elif delete_student == "no":
            print("Alright thanks for your answer!")
            break

        else: 
            print("You have given an unappropriate answer!")

    


addOnlyOneStudent(students_class)

print("\n")

print("**************************************")

print("\n")

deleteOnlyOneStudent(students_class)

print("\n")

print("**************************************")

print("\n")

print("Class of students: ")

for i in students_class:
    print(i)
