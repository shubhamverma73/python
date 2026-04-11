import os

print(os.name) # nt for windows and posix for linux
print(os.getcwd()) # current working directory
print(os.listdir()) # list of files and directories in the current working directory
print(os.path.exists("os.py")) # check if a file exists
print(os.path.isfile("os.py")) # check if it is a file
print(os.path.isdir("os.py")) # check if it is a directory
if not os.path.exists("new_directory"):
    os.mkdir("new_directory")
print(os.path.exists("new_directory")) # check if the new directory was created
print(os.listdir()) # list of files and directories in the current working directory
print(os.mkdir("new_directory1")) # create a new directory
print(os.rmdir("new_directory1")) # remove a directory
with open("new_file.txt", 'w') as f: pass  # create a new file
with open("new_file1.txt", 'w') as f: pass  # create a new file
print(os.remove("new_file1.txt")) # remove a file