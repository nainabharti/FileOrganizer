import os
import shutil

# File extensions for each category
FILE_CATEGORIES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"],
    "Documents": [".txt", ".pdf", ".docx", ".doc", ".pptx", ".ppt", ".xlsx", ".xls", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"]
}

OTHER_CATEGORY = "Others"


def get_category(extension):
    """Return the category for a file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category

    return OTHER_CATEGORY


def get_unique_path(destination_folder, filename):
    """Generate a unique path if the filename already exists."""
    destination_path = os.path.join(destination_folder, filename)

    if not os.path.exists(destination_path):
        return destination_path

    name, extension = os.path.splitext(filename)
    counter = 1

    while True:
        new_filename = f"{name}_{counter}{extension}"
        destination_path = os.path.join(destination_folder, new_filename)

        if not os.path.exists(destination_path):
            return destination_path

        counter += 1


def organize_files(folder_path):
    """Organize files into category folders."""
    categories = list(FILE_CATEGORIES.keys()) + [OTHER_CATEGORY]

    # Create category folders
    for category in categories:
        category_path = os.path.join(folder_path, category)
        os.makedirs(category_path, exist_ok=True)

    # Get the items present in the selected folder
    files = os.listdir(folder_path)

    moved_count = 0
    failed_count = 0
    skipped_count = 0

    for filename in files:
        source_path = os.path.join(folder_path, filename)

        # Skip folders
        if not os.path.isfile(source_path):
            skipped_count += 1
            continue

        # Identify the file extension
        _, extension = os.path.splitext(filename)
        category = get_category(extension)

        # Find the destination folder
        destination_folder = os.path.join(folder_path, category)

        # Avoid overwriting files with the same name
        destination_path = get_unique_path(
            destination_folder, filename
        )

        # Move the file safely
        try:
            shutil.move(source_path, destination_path)
            print(f"Moved: {filename} -> {category}")
            moved_count += 1

        except OSError as error:
            print(f"Failed to move {filename}: {error}")
            failed_count += 1

    # Display summary
    print("\n========== ORGANIZATION SUMMARY ==========")
    print(f"Files moved: {moved_count}")
    print(f"Files failed: {failed_count}")
    print(f"Folders skipped: {skipped_count}")
    print("==========================================")
    print("File organization completed!")


def main():
    """Run the file organizer."""
    print("===== PYTHON FILE ORGANIZER =====")
    folder_path = input(
        "Enter the folder path to organize: "
    ).strip().strip('"').strip("'")

    # Check whether the user entered a path
    if not folder_path:
        print("Error: Folder path cannot be empty.")
        return

    # Convert the path to an absolute path
    folder_path = os.path.abspath(
        os.path.expanduser(folder_path)
    )

    # Validate the folder
    if not os.path.exists(folder_path):
        print(f"Error: Folder does not exist: {folder_path}")
        return

    if not os.path.isdir(folder_path):
        print(f"Error: This path is not a folder: {folder_path}")
        return

    try:
        organize_files(folder_path)
    except OSError as error:
        print(f"Error while organizing folder: {error}")


if __name__ == "__main__":
    main()