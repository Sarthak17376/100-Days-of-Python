# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for rows in data:
#         if rows[1] != 'temp':
#             temperature.append(int(rows[1]))
#
# print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")

# print(data)
# print(data["day"])

# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# avg = data.temp.mean()
#
# print(avg)

# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# TinF = int(monday.temp)/5*9+32
# print(TinF)

# new database
data_dict = {
    "Students": ["Amy", "Laurel", "Polly"],
    "Marks": [45, 56, 78]
}

data = pandas.DataFrame(data_dict)
data.to_csv("New_csv.csv")
