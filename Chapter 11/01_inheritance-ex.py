# * Parent Class
class Vehicle:
    def start(self):
        print(" Vehicle started.")

# ^ Child class inheriting Vehicle
class Car(Vehicle):
    def play_music(self):
        print(" Playing music.")

# Creating an object of Car
my_car = Car()

# Calling methods
my_car.start()         # Inherited from Vehicle
my_car.play_music()    # Child's own method
