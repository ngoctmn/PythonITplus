import os

# Open file:
# Get file path
dirpath = os.path.dirname(__file__)
file = os.path.join(dirpath, 'lesson8_fileIO.txt')

# Open file (mode default: r = Read only)
open(file)
print('Open file with default mode.')

# Open file (mode: r+ = Read and Writte)
open(file, 'r+')
print('Open file with Read & Writte mode.')
