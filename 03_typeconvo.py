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

weight_lbs = input("Weight (lbs): ")
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

# Weight Calculator
weight = int(input('Weight: '))
unit = input('Its in (L)bs or (K)g ? ')

if unit.upper() == 'L':
    convert = weight * 0.45
    print(f'Your converted weight is {convert} kilos')
else:
    convert = weight/0.45
    print(f'Your converted weight is {convert} pounds')