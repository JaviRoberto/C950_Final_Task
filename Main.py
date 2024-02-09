import Packages
import pandas as pd
import Trucks
import datetime

pd.options.display.max_rows = 9999


class Main:
    package_sheet = pd.read_excel('packages.xlsx', skiprows=[1, 2, 3, 4, 5, 6, 7])

    package_list = []
    for index, row in package_sheet.iterrows():
        x = Packages.Packages(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        package_list.append(x)


    truck1 = Trucks.Trucks(16, 18, 8, 0, 0, "4001 South 700 East", 1,[1,4,7,10,13,16,19,22,25,28,31,34,37,40])

    truck2 = Trucks.Trucks(16, 18, 8, 0, 0, "4001 South 700 East", 2,(2,5,8,11,14,17,20,23,26,29,32,35,38))

    truck3 = Trucks.Trucks(16, 18, 8, 0, 0, "4001 South 700 East", 0,[3,6,9,12,15,18,21,24,27,30,33,36,39])
    # for i in range(39):
    # package_list[i].print_package()

    destinations = pd.read_excel('distance.xlsx', skiprows=[1, 2, 3, 4, 5, 6])

    destinations_list = destinations.to_dict(orient='records')


    print(package_list[1].print_package())
