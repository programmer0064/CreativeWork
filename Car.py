class Car:
    
    def __init__(self, brand, number_of_doors, speed):
        self.speed = speed
        self.number_of_doors = number_of_doors
        self.brand = brand

    def choiceOfCar(self):
        name_of_car = input("Which car do I need to compare with your criteria: ")
        if name_of_car in self.brand:
            print("Perfect the brand is one of your favorites.")
            speed_of_car = int(input("Type in the speed of your chosen car: "))
            if speed_of_car >= self.speed:
                print("Perfect the car has the minimum speed you wanted.")
                number_of_doors_of_car = int(input("Type in the numbers of the doors: "))
                if number_of_doors_of_car == self.number_of_doors:
                    print("The car has the perfect amount of doors.")
                    return True
                else:
                    print("The number of doors is not good.")
                    return False 
            else:
                print("It is too slow.")
                return False       
        else:
            print("It is not one of your favorite brands.")
            return False

while True:
    try:
        favorite_cars = [] 
        number_of_favorite_cars = int(input("How many favorite cars do you have: "))
        answer = isinstance(number_of_favorite_cars, int)
        if answer:
            i=0
            for i in range(number_of_favorite_cars):
                favorite_car = input(f"Give me your favorite brand name number {i+1}: ")
                favorite_cars.append(favorite_car)
            break
    except:
        print("Please type in a number!")    

#----------------------------------------------------------------------------------------------------

while True:
    try:
        number_of_doors = int(input("How many doors do you want: "))   
        if isinstance(number_of_doors, int):
            break
    except:
        print("Please type in a number!")          

while True:
    try:
        speed = int(input("Type in the minimum amount of speed of the car: "))         
        if isinstance(speed, int):
            break
    except:
        print("Please type in a number!")

#------------------------------------------------------------------------------------------------------

car1 = Car(favorite_cars, number_of_doors, speed)

print("\n")

if car1.choiceOfCar() == True:
    print("You should buy this car.")
else:
    print("Sorry this car is not for you.")

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

class Ferrari(Car):
    def __init__(self, brand, number_of_doors, speed, my_price):
        super().__init__(brand, number_of_doors, speed)
        self.price = my_price

    def compareCarPrice(self, price_of_car = int(input("How much does this Ferrari cost: "))):
        if price_of_car > self.price:
            return False

ferrari = Ferrari(favorite_cars, number_of_doors, speed, int(input("How much do you want to pay: ")))
too_expensive = ferrari.compareCarPrice()
if too_expensive == False:
    print("Sorry but the Ferrari is too expensive for you. Feel free to choose another car!")
else:
    print("Perfect.You can buy the car.")


        
