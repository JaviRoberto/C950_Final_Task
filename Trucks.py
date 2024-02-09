
class Trucks:

    def __init__(self,size, speed, time_departure, time_total, miles, address, driver, package):
        self.size = size
        self.speed = speed
        self.time_departure = time_departure
        self.time_total = time_total
        self.miles = miles
        self.address = address
        self.driver = driver
        self.package = package

    def print_truck(self):
        print(self.size)
        print(self.speed)
        print(self.time_departure)
        print(self.time_total)
        print(self.miles)
        print(self.address)
        print(self.driver)
        print(self.package)
