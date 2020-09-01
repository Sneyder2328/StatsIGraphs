import matplotlib.pyplot as plt


def get_array(file_name, *args):
    arr = []
    with open(file_name) as data_set_file:
        for line in data_set_file:
            data_row = line.replace("\n", "").split(",")
            data = []
            for arg in args:
                try:
                    value = int(data_row[arg])
                    data.append(value)
                except:
                    pass
            arr.append(data)
    arr.pop(0)
    return arr


years_and_price = get_array("train.csv", 19, 80)
years_and_price = sorted(years_and_price, key=lambda x: x[0])
# years_and_price = list(filter(lambda x: x[0] > 1920, years_and_price))
years_and_price = list(filter(lambda x: x[0] > 1920, years_and_price))

print(years_and_price)
print()

years_and_quality = get_array("train.csv", 19, 17)
years_and_quality = sorted(years_and_quality, key=lambda x: x[0])
print(years_and_quality)

plot1 = plt.figure(1)
plt.plot(list(map(lambda x: x[0], years_and_price)), list(map(lambda x: x[1], years_and_price)))
plt.xlabel('Año')
plt.ylabel('Precio de venta')
plt.draw()

plot2 = plt.figure(2)
plt.plot(list(map(lambda x: x[0], years_and_price)), list(map(lambda x: x[1], years_and_price)), 'ro', markersize=4,
         color="#46a5e5")
plt.xlabel('Año')
plt.ylabel('Precio de venta')
plt.draw()

plt.show()

# year_built_arr = list(map(lambda str: int(str), get_array("train.csv", 19)))
# sale_price_arr = list(map(lambda str: int(str), get_array("train.csv", 80)))
# print(year_built_arr)
# print(sale_price_arr)
#
