#!/usr/bin/python3
from DirHandler import DirHandler
from helpers import print_title, clear

# Used for production on the Ubuntu Machine that runs the SP-500 Scanner
UBUNTU_SERVER_INIT_DIR = ""
UBUNTU_LOCAL_TEMP_DIR = ""
UBUNTU_SERVER_TARGET_DIR = ""

# These are the directories used for testing on my personal Mac Machine.
MAC_SERVER_INIT_DIR = "/Users/edrdmolina/Desktop/SP-3000ExportDir"
MAC_LOCAL_TEMP_DIR = "/Users/edrdmolina/Desktop/TempTest"
MAC_SERVER_TARGET_DIR = "/Users/edrdmolina/Desktop/TargetTest"

# The path where the scanner exports to.
initial_path = MAC_SERVER_INIT_DIR

# Temporary directory where Ubuntu can rename directories and files on the local machine.
temp_path = MAC_LOCAL_TEMP_DIR

# the scannedimages folder where the weekly folders and scans reside.
target_path = MAC_SERVER_TARGET_DIR

is_run = True

if __name__ == "__main__":

    while is_run:
        print_title()

        roll_number = input("Input roll number (0123): ")

        relocator = DirHandler(initial_path, temp_path, target_path, roll_number)
        relocator.start()

        run_again = input("Are there more rolls? (Y/N): ").upper().strip()

        if run_again == "N":
            is_run = False

        clear()
