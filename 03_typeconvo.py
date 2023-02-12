birth_year = input('Birth year: ')


# age = 2019 - birth_year

# it will appear as int - str means 2019 - '2000'
# we will use type conversion
# int() = for converting string to integer
# float()
# bool()
print(type(birth_year))

age = 2023 - int(birth_year)

print(type(age))
print(age)
