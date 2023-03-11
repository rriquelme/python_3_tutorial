import os

# Get current path
print(os.getcwd())
# Change directory
os.chdir(os.getcwd())
# Check if it is a file
print(os.path.isfile('07_os.py'))
# Check if it is a directory
print(os.path.isdir(os.getcwd()))
# Join 2 paths or a path and a file
print(os.path.join(os.getcwd(),'07_os.py'))

# create a folder
os.mkdir('asd')
# remove the folder
os.rmdir('asd')