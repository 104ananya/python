course = "Python's course for Beginners"
# print(course) == print(course[0:])
# this will print whole string


# this will print last index
# speciality of python = negative indexing
print(course[-1])

# this will print from 0 to 3
print(course[0:3])

# this will exclude provided index
print(course[1:])

# it will start printing from first index, but it will exclude last 3 index
print(course[1:-3])
name = 'My name is "Ananya"'
print(name)


# [:] this is also used for copying the string
copy_name = name[:]
print(copy_name)

message = '''
Hi pal,
Here is our first message to you

Thank you,
The support team
'''

print(message)
