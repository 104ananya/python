# while loop
ind = 1
while ind <= 5:
    print('*' * ind)
    ind += 1
print("done")
# in python while loop can have optional else statement


# for loop
for item in 'Python':
    print(item)

for item in ['abc', 'pqr', 'xyz']:
    print(item)

for item in range(5, 10, 2):
    print(item)

price = [10, 20, 30]
total = 0
for item in price:
    total += item
print(f'Total value is {total}')


# Nested loops
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')


# draw f shape
f_letter = [5, 2, 5, 2, 2]
l_letter = [2, 2, 2, 2, 5]

print("Form letter F")
for x in f_letter:
    output = ''
    for x_count in range(x):
        output += 'X'
    print(output)

print("Form letter L")
for x in l_letter:
    output = ''
    for x_count in range(x):
        output += "X"
    print(output)