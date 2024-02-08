
class Trucks:

    def __init__(self,size, speed, time_left, miles, address):
        self.size = size
        self.speed = speed
        self.time_left = time_left
        self.miles = miles
        self.address = address

    def print_truck(self):
        print(self.size)
        print(self.speed)
        print(self.time_left)
        print(self.miles)
        print(self.address)