import os
import shutil

folder_path = "test_files"

files = os.listdir(folder_path)

image_extensions = [".png",".jpg",".jpeg",".gif"]
document_extensions = [".txt",".pdf",".docx",".doc"]
video_extensions = [".mp4",".wkv",".avi"]
music_extensions = [".mp3",".wav",".aac"]

categories = ["Images","Documents","Videos","Music","Others"]
for category in categories:
    category_path = os.path.join(folder_path, category) 
    os.makedirs(category_path,exist_ok=True)

for file in files:
    source_path = os.path.join(folder_path, file)
    if not os.path.isfile(source_path):
        continue
    name, extension = os.path.splitext(file)
    extension = extension.lower()

    if extension in image_extensions:
        category = "Images"
    elif extension in document_extensions:
        category = "Documents"
    elif extension in video_extensions:
        category = "Videos"
    elif extension in music_extensions:
        category = "Music"
    else:
        category = "Others"

    category_path = os.path.join(folder_path, category)
    destination_path = os.path.join(category_path, file)

    shutil.move(source_path, destination_path)

    print(f"Moved {file} to {category}")

print("File organization completed successfully!")
