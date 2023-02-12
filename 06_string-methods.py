course = 'Python For Beginners'
print(len(course))


course.upper()
print(course)   # Not modifying the original string
print(course.upper())

print(course.find('B'))     # case sensitive

print(course.replace('Beginners', 'Noobs'))

#  to check if word is in the string
print('Python' in course)

print(course.title())