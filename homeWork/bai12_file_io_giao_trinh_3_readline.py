import os

# Open file:

# Get file path
dirpath = os.path.dirname(__file__)
print(dirpath)
filepath = os.path.join(dirpath, 'lesson8_fileIO.txt')

# Open file
file = open(filepath, 'r+')

# Read file with size
# s = file.read(15)
# print('File content: ', s)


s1 = file.readline()
s2 = file.readline()
s3 = file.readline()
s4 = file.readline()
s5 = file.readline()

print('Line 1: ', s1)
print('Line 2: ', s2)
print('Line 3: ', s3)
print('Line 4: ', s4)
print('Line 5: ', s5)
