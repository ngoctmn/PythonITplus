import os

# Open file:

# Get file path
dirpath = os.path.dirname(__file__)
print(dirpath)
filepath = os.path.join(dirpath, 'lesson8_fileIO.txt')

# Open file
file = open(filepath, 'r+')

# Read file
str = file.read()
print('File content: ', str)

# Read file with size
s = file.read(15)
print('File content: ', s)
