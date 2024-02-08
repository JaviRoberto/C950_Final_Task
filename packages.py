
class Packages:

    print('Hello Package')

    def __init__(self, ID, address, city, state, zipcode, deadline, kilo, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.kilo = kilo
        self.status = status

    def print_package(self):
        print(self.ID)
        print(self.address)
        print(self.city)
        print(self.state)
        print(self.zipcode)
        print(self.deadline)
        print(self.kilo)
        print(self.status)

    #def status_set(self):

