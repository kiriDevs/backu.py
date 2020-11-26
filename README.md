# backu.py
An easy-to-use python backup-script.

## Where you can use it
Windows operating systems having both powershell and cmd.exe.
Tested on:
- Windows 10 Home

## What it can do
- Backup selected folders, together with subfolder and files, to another location using powershell commands
- Allow user to change folders to copy and destination by modifying a variable
- Name Backup-Folders with date and time automatically
- Allow user to change timestamp formatting template by modifying a variable
- Run without additional user input besides the original configuration
  - Can run fully automated via scheduling

## What is planned for the future
- Exclude specific subfolders or files
- Remove config from the script and put it in an own file (to make it easier to change something)
- Option to only store a single backup at a time (removes older ones)
- Using other file possibilities

## Further information
- Run the script with elevated permissions to avoid the script not being able to copy some files due to lacking permissions
- If copying system files or program files, copying some of these will fail due to the file being used
  - It is advised to close all programs before starting the script
- You WILL NEED to change some values in the python script itself to tell it what to copy. This is commented and pretty straight-forward.

## Reach out!
If you want to report a bug or request a feature, create an issue. If you know how to do it yourself, you can also make a change yourself and open a pull request. You can also ask questions via the issues tab.
