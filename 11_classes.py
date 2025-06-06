class Vehicle:

    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "Driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.engine = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engine, "Car at", self.speed)

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("MotorCycle")

        if(hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2

        self.doors = 0
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "Motorcycle at", self.speed)


car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)

print(mc1.wheels)
print(car1.engine)
print(car2.doors)

car1.drive(30)
car2.drive(40)
mc1.drive(50)