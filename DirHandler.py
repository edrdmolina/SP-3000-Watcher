from natsort import natsorted
from os import listdir, rename, path, scandir, stat
import time
import datetime
import shutil


class DirHandler:

    def __init__(self, initial_dir, temp_dir, target_dir, roll_number):
        self.initial_dir = initial_dir
        self.temp_dir = temp_dir
        self.target_dir = target_dir
        self.roll_number = roll_number

    @staticmethod
    def find_roll(initial_dir, roll_number):
        """
        -   Sort subdirectories from newest to oldest
        -   check each name until you find the one that ends with the roll number.
        """
        subdirectories = [f.path for f in scandir(initial_dir) if f.is_dir()]
        sorted_subdirectories = sorted(subdirectories, key=lambda x: stat(x).st_ctime, reverse=True)

        found_dir = ""

        for dir_path in sorted_subdirectories:
            last_four = dir_path[-4:]
            if last_four == roll_number:
                found_dir = dir_path

        if found_dir:
            print(f"Found Roll No. {roll_number}")
            time.sleep(10)
        else:
            print(f"No directory found with roll number: {roll_number}")
        return found_dir

    @staticmethod
    def get_monday():
        today = datetime.date.today()
        days_since_monday = today.weekday()
        monday = today - datetime.timedelta(days=days_since_monday)
        return monday.strftime('%m-%d-%y')

    @staticmethod
    def move_directory(old_dir, new_dir):
        try:
            shutil.move(old_dir, new_dir)
        except OSError as e:
            if e.errno == 95:
                pass
            elif e.errno == 2:
                pass

    @staticmethod
    def standardize_dir_name(name_input):
        if len(name_input) == 13:
            name_input = name_input[:2] + '-' + name_input[2:7] + '-' + name_input[9:]
        elif len(name_input) == 15:
            name_input = name_input[:2] + '-' + name_input[4:9] + '-' + name_input[11:]
        name_input = name_input.upper()
        return name_input

    @staticmethod
    def update_file_names(target_dir, order_name):
        print("Updating File Names. Please wait...")
        counter = 1
        files = natsorted(listdir(target_dir))

        for file in files:
            extension = str(path.splitext(file)[1]).lower()
            if extension == ".jpg":
                new_name = f"{order_name}-{counter:03d}.jpg"
                rename(path.join(target_dir, file), path.join(target_dir, new_name))
                counter += 1
            elif extension == ".jpeg":
                new_name = f"{order_name}-{counter:03d}.jpeg"
                rename(path.join(target_dir, file), path.join(target_dir, new_name))
                counter += 1
            elif extension == ".tiff":
                new_name = f"{order_name}-{counter:03d}.tiff"
                rename(path.join(target_dir, file), path.join(target_dir, new_name))
                counter += 1
            elif extension == ".tif":
                new_name = f"{order_name}-{counter:03d}.tif"
                rename(path.join(target_dir, file), path.join(target_dir, new_name))
                counter += 1
            time.sleep(0.10)

        print("Finished renaming files.")

    def start(self):
        """

        """
        # found roll is the roll dir path found in the export folder
        found_roll = self.find_roll(self.initial_dir, self.roll_number)

        if found_roll:
            """
                Successfully found the roll folder
                set up standardized name
                reset temp dir path and target dir path
            """
            standardized_name = self.standardize_dir_name(path.basename(found_roll))
            self.temp_dir = path.join(self.temp_dir, standardized_name)
            self.target_dir = path.join(self.target_dir, self.get_monday())
            self.target_dir = path.join(self.target_dir, standardized_name)

            self.move_directory(found_roll, self.temp_dir)
            self.update_file_names(self.temp_dir, standardized_name)
            self.move_directory(self.temp_dir, self.target_dir)

        else:
            return
