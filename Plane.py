class Plane:

    def __init__(self, name, altitude, speed):
        self.name = name
        self.altitude = altitude
        self.speed = speed

    def superFastPlane(self):
        if self.speed >= 1000:
            print(f"This plane with the speed {self.speed} super fast")
        
        else:
            print("This plane is not super fast")
    

