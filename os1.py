import os

# Get the current working directory
current_dir = os.getcwd()
print("Current Directory:", current_dir)
print('-----------------------------------------')

# List files and directories in the current directory
files_and_dirs = os.listdir(current_dir)
print("Files and Directories:", files_and_dirs)

print('-----------------------------------------')

# Create a new directory
new_dir = os.path.join(current_dir, 'new_directory')
os.mkdir(new_dir)
print("New Directory Created:", new_dir)


print('-----------------------------------------')

# Check if a path exists
exists = os.path.exists(new_dir)
print("Does the directory exist?", exists)


print('-----------------------------------------')

# Remove the directory
os.rmdir(new_dir)
print("Directory Removed:", new_dir)


print('-----------------------------------------')
