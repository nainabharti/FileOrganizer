Python File Organizer

A beginner-friendly Python project that automatically organizes files into folders based on their file extensions.

Features

- Accepts a folder path from the user.
- Checks whether the entered path exists and is a directory.
- Automatically creates category folders.
- Organizes images, documents, videos, and music.
- Moves unknown file types into an "Others" folder.
- Handles duplicate filenames without intentionally overwriting existing files.
- Handles common file-movement errors.
- Displays a summary of moved and failed files.

Categories

Category| Example Extensions
Images| ".png", ".jpg", ".jpeg", ".gif"
Documents| ".txt", ".pdf", ".docx", ".doc"
Videos| ".mp4", ".mkv", ".avi"
Music| ".mp3", ".wav", ".aac"
Others| Unrecognized extensions

Technologies Used

- Python 3
- "os" module
- "shutil" module

No external packages are required.

How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run the following command:

python main.py

6. Enter the path of the folder you want to organize when prompted.

Example

If the selected folder contains "photo.png" and "notes.txt", the program moves them into the "Images" and "Documents" folders, respectively.

Safety Note

The program moves files instead of copying them. Test it on a folder containing sample files before using it on important folders.

Future Improvements

- Add a graphical user interface.
- Add a preview mode before moving files.
- Add automated tests.

Author

Naina Bharti