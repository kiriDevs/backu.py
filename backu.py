# backu.py by kiriMCdev
# This script was made by kiriMCdev
# It is provided as-is, without any warranty, unless required by applicable law
# It is not supposed to be published or redistributed in any form, except explicitly permitted by kiriMCdev in writing.

# You NEED to change some values, obviously, as not every system is the same.
# Remember to use Backslashes (\) instead of normal slashes (/).
# REMEMBER TO ESCAPE ALL BACKSLASHES (\) WITH ANOTHER ONE (\\)

from os import system as syscall
from datetime import datetime

# ===== YOU NEED TO EDIT THESE VALUES ACCORDING TO YOUR NEEDS =====
folders_to_copy = ["C:\\Users", "C:\\Program Files", "C:\\Program Files (x86)"]  # Add a list of all folders you want
# to copy. Exclude the prefix from root_directory. You don't need to include every single subfolder. Every folder here
# is copied recursively.

destination = "H:\\Backup"  # Change to the path you want to copy the files to, preferably to an external drive,
# or network share or cloud service.

date_format_preset = "%Y-%m-%d_%H-%M"  # How the date will be formatted in the backup folder name. This will always
# resemble the time the backup was started at
#
# %Y = 4-digit year
# %m = month of year
# %d = day of month
# %H = hour of day
# %M = minute of hour
# For more information, visit the following website [https://www.programiz.com/python-programming/datetime/strftime]

prefix = "[backu.py] "  # How messages from the python script itself will distinguish from power-shell messages
# ===== STOP EDITING - YOU ARE DONE NOW =====

now = datetime.now()
now_string = now.strftime(date_format_preset)

try:
    # Creating folder for backup
    backup_folder = "{0}\\Backup-{1}".format(destination, now_string)
    syscall("mkdir {0}".format(backup_folder))

    copy_into = "{0}\\Backup".format(destination)
    # Copying specified folders
    for folder in folders_to_copy:
        print(prefix + "Now copying folder \"{0}\"".format(folder))
        command = "powershell cp -path {0} -destination {1} -recurse".format(folder, backup_folder)
        print(prefix + "Running \"{0}\"".format(command))
        syscall(command)
except Exception:
    print(prefix + "Unknown error completing Backup job. Exiting with code 1.")
    exit(1)

print(prefix + "Finished Backup job. Exiting with code 0.")
exit(0)
