names = ["Black", "Red", "Maroon", "Yellow"]
codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

colors = []

for i in range(len(names)):
    color = {
        "color_name": names[i],
        "color_code": codes[i]
    }

    colors.append(color)

print(colors)