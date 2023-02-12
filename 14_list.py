name = ['abc', 'xyz', 'pqr', 'str']

print(name)
print(name[-1])
print(name[2:])     # doesn't modify original list, simply return new list
print(name[1: 3])

name[0] = 'abcd'
print(name)

# largest number in the list
num = [3, 6, 2, 8, 4, 10]
max_num = num[0]
for i in num:
    if i > max_num:
        max_num = i
print(f'Maximum number is {max_num}')

# 2D list

# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print(matrix[0][1])

# List methods
numbers = [5, 2, 1, 7, 4]
numbers2 = numbers.copy()

print(numbers)
numbers.append(20)
print(numbers)
print(numbers2)

numbers.insert(4, 10)
numbers.remove(7)
numbers.pop()
print(numbers.index(5))
print(7 in numbers)
print(numbers)

numbers.sort()
numbers.reverse()
print(numbers)

# Remove duplicates in the list
list1 = [2, 3, 2, 4, 6, 3, 4, 6, 1]
unique = []

for i in list1:
    if i not in unique:
        unique.append(i)

print(f'Print list of unique elements : {unique}')








