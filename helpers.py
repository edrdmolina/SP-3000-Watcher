from os import system, name


def print_title():
    print("""
           _____   _____             ____     ___     ___     ___  
          / ____| |  __ \           |___ \   / _ \   / _ \   / _ \ 
         | (___   | |__) |  ______    __) | | | | | | | | | | | | |
          \___ \  |  ___/  |______|  |__ <  | | | | | | | | | | | |
          ____) | | |                ___) | | |_| | | |_| | | |_| |
         |_____/  |_|               |____/   \___/   \___/   \___/ 
    """)


def clear():
    """
        This function clears the terminal
    """
    # for windows
    if name == 'nt':
        return system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        return system('clear')
