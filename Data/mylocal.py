import os

# Get the current directory
mylocal = os.getcwd()
print("Current Directory:", mylocal)

# List files and directories in the current directory
contents = os.listdir(mylocal)
print("Contents:")
for item in contents:
    print(item)
