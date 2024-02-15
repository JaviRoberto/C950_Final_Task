import datetime

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

def get_packages():
    package_sheet = pd.read_excel('packages.xlsx', skiprows=[1, 2, 3, 4, 5, 6,7])
    package_list = []
    for index, row in package_sheet.iterrows():
        x = Packages.Packages(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        package_list.append(x)
    return package_list

def sort_packages():
    arr = get_packages()
    n = len(arr)
    swapped = False
    for i in range(1):
        for i in range(n):
            for j in range(0, n-i-2):
                if find_distance(arr[j].address,arr[j+1].address) > find_distance(arr[j].address,arr[j+2].address):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr




class Main:
    package_list = get_packages()

    #print("Welcome to the WGUPS routing service by Javier Ochoa!")
    #input("Press Enter to sort packages into most efficient delivery pattern")


    truck1 = Trucks.Trucks(16, 18, 8, 0, 0, "4001 South 700 East", 1,
                           [28,32,2,4,5,6,8,9,10,11,12,17,18,21,22,23,24,26,27,28])
    # Packages #6, #25, #28, #32 arrived late on a flight and are not available to leave the hub before 9:05 a.m..

    truck2 = Trucks.Trucks(16, 18, 8, 0, 0, "4001 South 700 East", 2,
                           [1,13,14,15,16,19,20,3,18,36,38,37]) #40 is taken out!!!!!
    # Packages #13, #14, #15. #16, #19, and #20 must go out for delivery on the same truck.
    #15 needs to be delivered on or before 9:00 am
    # Packages #3, #18, #36, and #38 may only be delivered by truck 2.


    truck3 = Trucks.Trucks(16, 18, 8, 0, 0, "4001 South 700 East", 0,
                           [6,9,25,29,30,31,33,34,35,37,39])
    # Packages #1, 6, 9 13, 14, 16, 20, 25, 29, 30, 31, 34, 37 and 40 need to be delivered on or before 10:30 am


# Two drivers and three trucks are available. So, no more than two trucks can be away from the hub at the same time.
# The trucks move at a constant speed of 18 miles per hour or 0.3 miles per minute.
# Each truck can carry a maximum of 16 packages.



# Package #15 needs to be delivered on or before 9:00 am.
# Packages #2-5, #7-12, #17-19, #21-24, #26-28, #32-33, #35-36, and #38-39 can be delivered by the end of the day (EOD) which would be 5:00 pm, so there can be some flexibility exercised as regards these packages.


#TRUCK 1
    countz = 0.0
    total_countz = 0.0
    truck_packages_array = truck1.get_packages()
    current_time = datetime.timedelta(0,0,0,0,0,8,)
    for pacakge_number in truck_packages_array:
        package_object = package_list[pacakge_number -1]
        package_object2 = package_list[pacakge_number]
        countz += float(find_distance(package_object.address,package_object2.address))
        total_countz += countz
        current_time += datetime.timedelta(minutes=(countz/18))
        truck1.time_total = current_time
        print("Truck 1 has delivered package",package_object.ID, "to", package_object.address, "at time", truck1.time_total)
    print("Truck 1 total distance is",int(countz), "miles")

    countz = 0.0
    truck_packages_array = truck2.get_packages()
    current_time = datetime.timedelta(0,0,0,0,0,8,)
    for pacakge_number in truck_packages_array:
        package_object = package_list[pacakge_number -1]
        package_object2 = package_list[pacakge_number]
        countz += float(find_distance(package_object.address,package_object2.address))
        current_time += datetime.timedelta(minutes=countz)
        truck1.time_total = current_time
        print("Truck 2 has delivered package",package_object.ID, "to", package_object.address, "at time", truck1.time_total)
    print("Truck 2 total distance is",int(countz), "miles")

    countz = 0.0
    truck_packages_array = truck3.get_packages()
    current_time = datetime.timedelta(0,0,0,0,0,8,)
    for pacakge_number in truck_packages_array:
        package_object = package_list[pacakge_number-1]
        package_object2 = package_list[pacakge_number]
        countz += float(find_distance(package_object.address,package_object2.address))
        current_time += datetime.timedelta(minutes=countz)
        truck1.time_total = current_time
        print(countz, "Truck 3 has delivered package",package_object.ID, "to", package_object.address, "at time", truck1.time_total)
    print("Truck 1 total distance is",int(countz), "miles")


for i in sort_packages():
    print(i.ID, end=",")






