import math

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors_names = ["Black", "Gray", "Cinnamon"]
fur_colors_count = []

for colors in fur_colors_names:
    count = len(data[data["Primary Fur Color"] == colors])
    fur_colors_count.append(count)

print(fur_colors_count)

squirrels = {
    "Fur Color": fur_colors_names,
    "Count": fur_colors_count
}

final = pandas.DataFrame(squirrels)
final.to_csv("Squirrel_census.cvs")
