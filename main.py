#!/usr/bin/python3
from DirHandler import DirHandler
from helpers import print_title, clear

# Used for production on the Ubuntu Machine that runs the SP-500 Scanner
UBUNTU_SERVER_INIT_DIR = "/run/user/1000/gvfs/afp-volume:host=GuruBibliotheca.local,user=gurubibliotheca,volume=Vault/Coastal Film Lab/SP-3000ExportDir"
UBUNTU_LOCAL_TEMP_DIR = "/home/coastal/Pictures/SP-3000-Temp-Dir"
UBUNTU_SERVER_TARGET_DIR = "/run/user/1000/gvfs/afp-volume:host=GuruBibliotheca.local,user=gurubibliotheca,volume=Vault/Coastal Film Lab/scannedimages"

# These are the directories used for testing on my personal Mac Machine.
MAC_SERVER_INIT_DIR = "/Users/edrdmolina/Desktop/SP-3000ExportDir"
MAC_LOCAL_TEMP_DIR = "/Users/edrdmolina/Desktop/TempTest"
MAC_SERVER_TARGET_DIR = "/Users/edrdmolina/Desktop/TargetTest"

# The path where the scanner exports to.
initial_path = UBUNTU_SERVER_INIT_DIR

# Temporary directory where Ubuntu can rename directories and files on the local machine.
temp_path = UBUNTU_LOCAL_TEMP_DIR

# the scannedimages folder where the weekly folders and scans reside.
target_path = UBUNTU_SERVER_TARGET_DIR

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
        
        # Canceled clearing to keep a log of rolls done
        # clear()
