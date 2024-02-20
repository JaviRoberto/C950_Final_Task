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


def find_distance(address1, address2):  # given two addreses, finds distance. NOT DONE

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
        else:
            pass
    for x in range(len(address_array)):
        if address2 == address_array[x][2]:
            number2 = address_array[x][0]
        else:
            pass

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

    # add code that can scan distances. given the number of the two addreses!

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
    package_sheet = pd.read_excel('packages.xlsx', skiprows=[1, 2, 3, 4, 5, 6, 7])
    package_list = []
    for index, row in package_sheet.iterrows():
        x = Packages.Packages(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        package_list.append(x)
    return package_list


def sorting(arr):
    n = len(arr)
    holder_array = []
    min_distance = 100
    i = 0
    second = arr[1]
    nullarray = [True for _ in range(40)]
    first = arr[0]
    nuller = None
    holder_array.append(arr[0])
    while i in range(len(arr) - 1):
        for j in range(1, len(arr)):
            if nullarray[j] is False:
                continue
            else:
                distance = float(find_distance(first.address, arr[j].address))
                if first.ID == arr[j].ID:
                    continue
                elif distance < min_distance:
                    min_distance = distance
                    second = arr[j]
                    nuller = j
                else:
                    continue
        holder_array.append(second)
        nullarray[nuller] = False
        first = second
        i += 1
        min_distance = 100

    return holder_array


class Main:
    print("Welcome to the WGUPS Delivery System by Javier Ochoa")
    input("Press Enter to load trucks based on Package requirments")
    package_list = get_packages()

    # print("Welcome to the WGUPS routing service by Javier Ochoa!")
    # input("Press Enter to sort packages into most efficient delivery pattern")

    truck1 = Trucks.Trucks(16, 18, 8, 0, 0, "4001 South 700 East", 1,
                           [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40])  # 40 belongs here

    truck2 = Trucks.Trucks(16, 18, 8, 0, 0, "4001 South 700 East", 2,
                           [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39])

    truck3 = Trucks.Trucks(16, 18, 8, 0, 0, "4001 South 700 East", 0,
                           [2, 33, 28, 4, 32, 6, 11, 25, 7, 10, 5, 8, 9])

    print("Trucks have been loaded.")
    print("Truck 1 has packages: ", truck1.package)
    print("Truck 2 has packages: ", truck2.package)
    print("Truck 3 has packages: ", truck3.package)
    input("Press Enter to organize the truck packages in an efficient manner using Javier's sorting fuction!")

    truckarraytemp = truck1.package
    temp_array = []
    temp_array2 = []
    for pacakge in truckarraytemp:
        temp_array.append(package_list[pacakge - 1])
    temp_sorted = sorting(temp_array)
    truck1.package = None
    for v in temp_sorted:
        temp_array2.append(v.ID)
    truck1.package = temp_array2

    # sorts truck 2
    truckarraytemp = truck2.package
    temp_array = []
    temp_array2 = []
    for pacakge in truckarraytemp:
        temp_array.append(package_list[pacakge - 1])
    temp_sorted = sorting(temp_array)
    truck2.package = None
    for v in temp_sorted:
        temp_array2.append(v.ID)
    truck2.package = temp_array2

    print("")

    truckarraytemp = truck3.package
    temp_array = []
    temp_array2 = []
    for pacakge in truckarraytemp:
        temp_array.append(package_list[pacakge - 1])
    temp_sorted = sorting(temp_array)
    truck3.package = None
    for v in temp_sorted:
        temp_array2.append(v.ID)
    truck3.package = temp_array2

    print("Trucks packages have been organized in order of delivery efficacy!")
    print("Truck 1 has packages: ", truck1.package)
    print("Truck 2 has packages: ", truck2.package)
    print("Truck 3 has packages: ", truck3.package)
    input("Press Enter to start the day and send the trucks on their way to deliver packages!")

    # Two drivers and three trucks are available. So, no more than two trucks can be away from the hub at the same time.
    # The trucks move at a constant speed of 18 miles per hour or 0.3 miles per minute.
    # Each truck can carry a maximum of 16 packages.

    # Package #15 needs to be delivered on or before 9:00 am.
    # Packages #2-5, #7-12, #17-19, #21-24, #26-28, #32-33, #35-36, and #38-39 can be delivered by the end of the day (EOD) which would be 5:00 pm, so there can be some flexibility exercised as regards these packages.

    # TRUCK 1
    total_countz = 0.0000001
    truck_packages_array = truck1.get_packages()
    current_time = datetime.timedelta(0, 0, 0, 0, 0, 8, )
    first_package = package_list[truck1.package[0]-1]
    countz = float(find_distance("4001 South 700 East", first_package.address))
    current_time += datetime.timedelta(minutes=(countz * 60 / 18))
    truck1.time_total = current_time
    print("Truck 1 has left the WGU hub and delivered package", first_package.ID, "to", first_package.address, "at time",
          truck1.time_total)
    for i in range(1, len(truck_packages_array)):
        package1 = truck_packages_array[i - 1]
        package2 = truck_packages_array[i]
        package_object = package_list[package1 - 1]
        package_object2 = package_list[package2 - 1]  # WRONG, IT IS TAKING OBJECT FORM ARRAY
        countz = float(find_distance(package_object.address, package_object2.address)) + .000000001
        total_countz += countz
        current_time += datetime.timedelta(minutes=(countz * 60 / 18))
        truck1.time_total = current_time
        # print(find_distance(package_object.address,package_object2.address), "distance")
        # print(package_object.ID, "==", package1,package_object2.ID,"==", package2)
        print("Truck 1 has delivered package", package_object2.ID, "to", package_object.address, "at time",
              truck1.time_total)
    truck1.miles = int(total_countz)
    print("Truck 1 total distance is", int(total_countz), "miles")


    # TRUCK 2
    total_countz = 0.0000001
    truck_packages_array = truck2.get_packages()
    current_time = datetime.timedelta(0, 0, 0, 0, 0, 8, )
    first_package = package_list[truck2.package[0]-1]
    countz = float(find_distance("4001 South 700 East", first_package.address))
    current_time += datetime.timedelta(minutes=(countz * 60 / 18))
    truck2.time_total = current_time
    print("Truck 2 has left the WGU hub and delivered package", first_package.ID, "to", first_package.address, "at time",
          truck2.time_total)
    for i in range(1, len(truck_packages_array)):
        package1 = truck_packages_array[i - 1]
        package2 = truck_packages_array[i]
        package_object = package_list[package1 - 1]
        package_object2 = package_list[package2 - 1]  # WRONG, IT IS TAKING OBJECT FORM ARRAY
        countz = float(find_distance(package_object.address, package_object2.address))
        total_countz += countz
        current_time += datetime.timedelta(minutes=(countz * 60 / 18))
        truck2.time_total = current_time
        # print(find_distance(package_object.address,package_object2.address), "distance")
        # print(package_object.ID, "==", package1,package_object2.ID,"==", package2)
        print("Truck 2 has delivered package", package_object2.ID, "to", package_object.address, "at time",
              truck2.time_total)
    truck2.miles = int(total_countz)
    print("Truck 2 total distance is", int(total_countz), "miles")

    # TRUCK 3
    total_countz = 0.0000001
    truck_packages_array = truck3.get_packages()
    current_time = datetime.timedelta(0, 0, 0, 0, 0, 9, )
    first_package = package_list[truck3.package[0]-1]
    countz = float(find_distance("4001 South 700 East", first_package.address))
    current_time += datetime.timedelta(minutes=(countz * 60 / 18))
    truck2.time_total = current_time
    print("Truck 3 has left the WGU hub and delivered package", first_package.ID, "to", first_package.address, "at time",
          truck3.time_total)
    for i in range(1, len(truck_packages_array)):
        package1 = truck_packages_array[i - 1]
        package2 = truck_packages_array[i]
        package_object = package_list[package1 - 1]
        package_object2 = package_list[package2 - 1]  # WRONG, IT IS TAKING OBJECT FORM ARRAY
        countz = float(find_distance(package_object.address, package_object2.address))
        total_countz += countz
        current_time += datetime.timedelta(minutes=(countz * 60 / 18))
        truck3.time_total = current_time
        # print(find_distance(package_object.address,package_object2.address), "distance")
        # print(package_object.ID, "==", package1,package_object2.ID,"==", package2)
        print("Truck 3 has delivered package", package_object2.ID, "to", package_object.address, "at time",
              truck3.time_total)
    truck3.miles = int(total_countz)
    print("Truck 3 total distance is", int(total_countz), "miles")


    print("Total Distance for all trucks is", truck1.miles + truck2.miles + truck3.miles, "miles.")
# for i in sort_packages():
# print(i.ID, end=",")
