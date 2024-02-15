import rows

import Packages
import pandas as pd
import Trucks
import csv

pd.options.display.max_rows = 9999


# todo add package info from object tp print, time delivered, and other stuff
# todo introduce alogrith to cut down milage, get smallest number, implimnet
# todo do tasks write up for both papers, task 1 and task 2.
# todo shceudel meeitng with professor before submiting

number1 = 0
number2 = 0

print("Welcome to the WGUPS routing service by Javier Ochoa! Please wait while data is accessed and Trucks are sent out. ")

def find_distance(address1, address2): #given two addreses, finds distance. NOT DONE
    address_array = []
    address_sheet_names = "new_addressCSV.csv"

    with open(address_sheet_names, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            address_array.append(row)

    # search and find array

    for i in range(len(address_array)):
        if address1 == address_array[i][2]:
            number1 = address_array[i][0]
        else: pass
    for x in range(len(address_array)):
        if address2 == address_array[x][2]:
            number2 = address_array[x][0]
        else: pass

    if address1 == "4001 South 700 East":
        number1 = 0

    elif address2 == "4001 South 700 East":
        number2 = 0

    address_sheet = "new_distanceCSV.csv"

    # initializing the titles and rows list
    #
    distance_array = []

    with open(address_sheet, 'r') as csvfile:  #
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            distance_array.append(row)

    #add code that can scan distances. given the number of the two addreses!

    distance_array = []
    address_sheet = "new_distanceCSV.csv"

    with open(address_sheet, 'r') as csvfile:  #
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            distance_array.append(row)

    convert_number1 = int(number1)
    convert_number2 = int(number2)
    if convert_number1 > convert_number2:
        x = convert_number1 - 1
        y = convert_number2
    else:
        y = convert_number1
        x = convert_number2 - 1
    return (distance_array[x][y])
            # , x, y, number1, number2)


    # def get_address(package_num):



class Main:


    package_sheet = pd.read_excel('packages.xlsx', skiprows=[1, 2, 3, 4, 5, 6])

    package_list = []
    for index, row in package_sheet.iterrows():
        x = Packages.Packages(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        package_list.append(x)

    truck1 = Trucks.Trucks(16, 18, 8, 0, 0, "4001 South 700 East", 1,
                           [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40])

    truck2 = Trucks.Trucks(16, 18, 8, 0, 0, "4001 South 700 East", 2,
                           [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38])

    truck3 = Trucks.Trucks(16, 18, 8, 0, 0, "4001 South 700 East", 0,
                           [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])
    # for i in range(39):
    # package_list[i].print_package()

    destinations = pd.read_excel('distance.xlsx', skiprows=[1, 2, 3, 4, 5, 6])

    destinations_list = destinations.to_dict(orient='records')

    # print(destinations_list.keys())
    # print(package_list[1].print_package())

    # for i in range(39):
    # package_list[i].print_package()

    testdic = {"Ford": ["mustang", "ecoboost", "explorer"], "Porsche": "911", "Toyota": "Prius"}

    address_sheet = "new_distanceCSV.csv"

    # initializing the titles and rows list
    #
    distance_array = []

    with open(address_sheet, 'r') as csvfile:  #
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            distance_array.append(row)

    address_array = []
    address_sheet_names = "new_addressCSV.csv"

    with open(address_sheet_names, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            address_array.append(row)

    # get total number of rows
    # print("Total no. of rows: %d" % csvreader.line_num)  # gets new_address names related to numbers
    # for i in range(len(distance_array)):
        # print(distance_array[i][0])
    # print(address_array[0][3])


    # print(find_distance("300 State St", "2835 Main St"))

    truck_packages_array = []
    i = 1
    count = 0
    package_in_place = 0
    package_in_place2 = 0
    package_address2 ="zero"
    truck_miles = 0

    while i < 14:
        truck1.driver = 1
        truck_packages_array = truck1.get_packages()
        package_in_place = package_list[truck_packages_array[i-1]]
        package_address = package_in_place.get_addresz()
        package_in_place2 = package_list[truck_packages_array[i]]
        package_address2 = package_in_place2.get_addresz()
        # print((package_address, package_address2))
        # print(find_distance(package_address, package_address2))
        count += float(find_distance(package_address, package_address2))
        placeholder_array = truck1.get_packages()
        print("Package",package_in_place.ID, "delivered by truck 1 to ", package_address) #xxxxxxxxxxxxx
        i += 1
    print("Package",package_in_place2.ID, "delivered by truck 1 to", package_address2), "at time, with all package info"
    time = count / 18
    truck1.time_total = time

    print("Truck 1 has traveled", count.__ceil__(), "miles, with driver", truck1.driver, "and a total time of", truck1.time_total,"hours",)
    truck3.driver = 0
    truck3.driver = 1
    print('Driver 1 has swtiched to truck 3')



###############
    truck_packages_array = []
    i = 1
    count = 0
    package_in_place = 0
    package_in_place2 = 0
    package_address2 ="zero"
    truck_miles = 0
    while i < 13:
        truck2.driver = 2
        truck_packages_array = truck2.get_packages()
        package_in_place = package_list[truck_packages_array[i-1]]
        package_address = package_in_place.get_addresz()
        package_in_place2 = package_list[truck_packages_array[i]]
        package_address2 = package_in_place2.get_addresz()
        # print((package_address, package_address2))
        # print(find_distance(package_address, package_address2))

        count += float(find_distance(package_address, package_address2))
        placeholder_array = truck3.get_packages()
        print("Package",package_in_place.ID, "delivered by truck 2 to", package_list[package_in_place.ID].address)
        i += 1
    print("Package",package_in_place2.ID, "delivered by truck 2 to ", package_address2)


    time = count / 18
    truck2.time_total = time
    print("Truck 2 has traveled", count.__ceil__(), "miles, with driver", truck2.driver, "and a total time of", truck2.time_total,"hours",)



    truck_packages_array = []
    i = 1
    count = 0
    package_in_place = 0
    package_in_place2 = 0
    package_address2 = "zero"
    truck_miles = 0
    while i < 13:
        truck_packages_array = truck3.get_packages()
        package_in_place = package_list[truck_packages_array[i-1]]
        package_address = package_in_place.get_addresz()
        package_in_place2 = package_list[truck_packages_array[i]]
        package_address2 = package_in_place2.get_addresz()
        # print((package_address, package_address2))
        # print(find_distance(package_address, package_address2))

        count += float(find_distance(package_address, package_address2))
        placeholder_array = truck3.get_packages()
        print("Package",package_in_place.ID, "delivered by truck 3 to", package_list[package_in_place.ID].address)
        i += 1
    print("Package",package_in_place2.ID, "delivered by truck 3 to ", package_address2)
    time = count / 18
    truck3.time_total = time
    print("Truck 3 has traveled", count.__ceil__(), "miles, with driver", truck3.driver, "and a total time of", truck3.time_total,"hours",)










