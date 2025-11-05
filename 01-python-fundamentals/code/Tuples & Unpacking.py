info = ("Adil", 26, "London")
print("Original:", info)

name, age, city = info
print(name)
print(age)
print(city)

info_list = list(info)
info_list[2] = "Dubai"
info = tuple(info_list)
print(info == info_list)
print(id(info) == id(info_list))

print("Updated:", info)