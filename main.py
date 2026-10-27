import os

folder_path = "test_files"

files = os.listdir(folder_path)

image_extensions = [".png",".jpg",".jpeg",".gif"]
document_extensions = [".txt",".pdf",".docx",".doc"]
video_extensions = [".mp4",".wkv",".avi"]
music_extensions = [".mp3",".wav",".aac"]

for file in files:
    file_path = os.path.join(folder_path, file)
    if not os.path.isfile(file_path):
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
    print(f"{file} -> {category}")

categories = ["Images","Documents","Videos","Music","Others"]
for category in categories:
    category_path = os.path.join(folder_path, category) 
    os.makedirs(category_path,exist_ok=True)
print("Category folders created successfully!")
