import os
from datetime import datetime
from pathlib import Path

# -----------------------------
# Logger (Context Manager)
# -----------------------------
class FileLogger:
    def __init__(self, log_file="file_manager.log"):
        self.log_file = log_file

    def __enter__(self):
        self.file = open(self.log_file, "a")
        return self

    def log(self, message):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.file.write(f"[{time}] {message}\n")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# -----------------------------
# Generator: stream files
# -----------------------------
def file_stream(directory):
    for item in os.scandir(directory):
        if item.is_file():
            yield item


# -----------------------------
# Smart File Manager
# -----------------------------
class SmartFileManager:
    FILE_TYPES = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".txt", ".docx"],
        "Videos": [".mp4", ".mkv"],
        "Music": [".mp3", ".wav"],
        "Archives": [".zip", ".rar"],
        "Scripts": [".py"]
    }

    def __init__(self, directory):
        self.directory = Path(directory)

    def organize(self):
        with FileLogger() as logger:
            logger.log(f"Started organizing: {self.directory}")

            for file in file_stream(self.directory):
                self._sort_file(file, logger)

            logger.log("Finished organizing files")

    def _sort_file(self, file, logger):
        extension = file.path.lower()
        for folder, extensions in self.FILE_TYPES.items():
            if any(extension.endswith(ext) for ext in extensions):
                self._move_file(file, folder, logger)
                return

        self._move_file(file, "Others", logger)

    def _move_file(self, file, folder_name, logger):
        target_dir = self.directory / folder_name
        target_dir.mkdir(exist_ok=True)

        target_path = target_dir / file.name

        try:
            os.rename(file.path, target_path)
            logger.log(f"Moved {file.name} → {folder_name}")
        except Exception as e:
            logger.log(f"Error moving {file.name}: {e}")


# -----------------------------
# Run the program
# -----------------------------
if __name__ == "__main__":
    path = input("Enter directory to organize: ").strip()

    if not os.path.isdir(path):
        print("❌ Invalid directory")
    else:
        manager = SmartFileManager(path)
        manager.organize()
        print("✅ Files organized successfully!")
