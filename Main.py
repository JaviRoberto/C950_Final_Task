import Packages
import pandas as pd

pd.options.display.max_rows = 9999


class Main:
    package_sheet = pd.read_excel('packages.xlsx', skiprows=[1, 2, 3, 4, 5, 6, 7])

    package_list = []

    for index, row in package_sheet.iterrows():
        x = Packages.Packages(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        package_list.append(x)

    for i in range(39):
        package_list[i].print_package()
