#Search files in a directory and subdirectories for a given file extension

import os
import sys
import argparse
import logging
import time
import datetime
import shutil

# Set up command line arguments
parser = argparse.ArgumentParser(description='Search files in a directory and subdirectories for a given file extension')

parser.add_argument('-d', '--directory', help='Directory to search', required=False)
parser.add_argument('-e', '--extension', help='File extension to search for', required=False)

args = parser.parse_args()

# Set up variables
directory = "E:\Photos\whatsapp-images"
extension = ".JPG"
file_list = []

# Check if directory exists
if not os.path.exists(directory):
    print('Directory does not exist')
    sys.exit()

# Check if directory is a directory
if not os.path.isdir(directory):
    print('Path is not a directory')
    sys.exit()
    
# Check if extension is valid
if not extension.startswith('.'):
    print('Extension must start with a period')
    sys.exit()
    
# Walk through directory and subdirectories
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(extension):
            file_list.append(os.path.join(root, file))

# Print results
count = 0
print('Files found:')
for file in file_list:
    count += 1
    #print(file)

print('Total files found: ', count)

# Create new directory
new_directory = os.path.join(directory, 'new')
if not os.path.exists(new_directory):
    os.makedirs(new_directory)
print('New directory created: ', new_directory)
    
copied_count = 0
#Copy files to the new directory
for file in file_list:
    copied_count += 1
    shutil.copy(os.path.join(directory, file), new_directory)
#print(os.path.join(new_directory, file))
#print('File copied: ', file)
print('Total files copied: ', copied_count)
