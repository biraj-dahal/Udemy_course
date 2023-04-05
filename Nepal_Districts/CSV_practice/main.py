import csv
import pandas
"""
# Using csv file to read
# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
# print(temp)

# Using pandas to retrieve data
data = pandas.read_csv("weather_data.csv")
dictionary_form = data.to_dict()
print(dictionary_form)

# list_form_each_column
list_form = data["condition"].to_list()
print(list_form)
print(data["temp"].mean())
print(data["temp"].max())
print(data.day) # same as data["day"]

# get Row
print(data[data.day == "Thursday"])
print(data[data.temp == data.temp.max()])

# particular row's value
print((data[data.day == "Monday"].temp * 9 / 5) + 32)

# create dataframe from python data.
dict_data = {
    "students": ["Amy", "Biraj", "Alison"],
    "scores": [60, 70, 80]
}
data = pandas.DataFrame(dict_data)
data.to_csv("new_data.csv")
print(data)
"""

whole_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_list = whole_data["Primary Fur Color"].to_list()
unique_list = list(set(color_list))
outfile_data = {
    "Fur Color": unique_list,
    "Count": [color_list.count(color) for color in unique_list],
}
data = pandas.DataFrame(outfile_data)
data.to_csv("Count_to_Color.csv")

