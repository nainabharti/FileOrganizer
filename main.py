import os

folder_path = "test_files"

files = os.listdir(folder_path)

for file in files:
    print(file)