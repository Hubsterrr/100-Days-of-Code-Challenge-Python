import pandas

# with open("weather_data.csv") as file:
#     data = file.readlines()
#
#
# print(data)
#
# import csv
#
#
# temperatures = []
#
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
# print(temperatures)

#
# data = pandas.read_csv("weather_data.csv")
#
#
# monday = data[data.day == "Monday"]
# monday_farenheit = (monday.temp * 1.8 + 32)
#
# print(monday_farenheit)

### Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_count = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

output_data = pandas.DataFrame(squirrel_count)
output_data.to_csv("squirrel_count.csv")












