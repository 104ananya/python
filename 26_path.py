from pathlib import Path

# Absolute path
# Relative path

# create a  path object become Path is a class

path = Path("ecommerce")

# to check if directory exists or not
print(path.exists())

path2 = Path("emails")

# to make directory
print(path2.mkdir())

# to remove directory
print(path2.rmdir())

# to print all the file with .py extension --- *.py
# to print all the file in folder -- *
path3 = Path()
for file in path3.glob('*.py'):
    print(file)
