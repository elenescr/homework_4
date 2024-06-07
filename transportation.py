class Transport:
    steering_wheel = 1
    weight = 5000
    windshield = "59 inches X 31.5 Inches"
    headlights = "white"
    def __init__(self, type, model, colour):
        self.type = type
        self.model = model
        self.colour = colour

    @staticmethod
    def door_lock():
        print("The doors are locked")
    @classmethod
    def colour_of_lights(cls):
        print(f"Headlight's colour is {cls.headlights}.")

    @classmethod
    def windshield_size(cls):
        print(f"vehicle's windshield size is {cls.windshield}.")
    def voice_assistant (self):
        print(f"Hello, welcome to {self.model}!")
    def vehicle_info (self) :
        print (f"I'm {self.type} and my colour is {self.colour}.")

    def __repr__(self):
        return f"My transport type is {self.type},model- {self.model} and {self.type}'s colour is {self.colour}."


vehicle1 = Transport("car","BMW x5", "black")
vehicle2 = Transport("motorcycle","Honda Super Cub", "red")
vehicle3 = Transport("car","Toyota Camry", "silver")
vehicle4 = Transport("bus","MAN ND323F", "mint")
vehicle5 = Transport("trailer","FREIGHTLINER eCascadia", "blue")

print(vehicle5)
vehicle4.vehicle_info()
print(f"my vehicle has {vehicle3.steering_wheel} steering wheel.")
vehicle1.door_lock()
vehicle2.voice_assistant()
vehicle4.windshield_size()
vehicle5.colour_of_lights()