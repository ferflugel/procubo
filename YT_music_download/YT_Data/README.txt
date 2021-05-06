-------------------------------------------------------------------------------------------------------
PRE-REQUISITES:

* REMINDER: For now this program is only supported for the Windows OS.
* You'll have to have Python (version >= 3.0) installed on your system and in your system variables.
* Check that the 'os', 'shutil', and 'time' modules run natively in your system, otherwise the program
will crash.

-------------------------------------------------------------------------------------------------------
If you run into library and/or compatibility issues, try manually installing the following libraries:

Required libraries:
* Pafy
* Youtube-dl
* Shutil
* PyDub
* Mutagen
* Simple_image_download

-------------------------------------------------------------------------------------------------------
NEXT STEPS:

Step 1: Download the entire 'YT_Data' structure from Github and extract it. Then, run the file
'DownloadPlaylist.py', either by double-clicking it on File Explorer, or running it on the terminal
(command prompt) through "python DownloadPlaylist.py" (or "python3 DownloadPlaylist.py", in case you
have various versions of Python installed on your system). Take note of the folders the program
displays on the output, you will need them later on...



Step 2: Click on the Windows search bar and type "Edit the system environment variables" and press
'Enter'. The system might ask for permission to make changes to your device, if so, click on "Yes".
On the bottom-right of the window that opened, click on "Environment Variables...". On the "User
variables...", find "Path" e click on "Edit". Hit "New", and with the folder the program printed
earlier (the one that ends with '\bin'), paste the whole path in the entry that it opened. Hit "OK"
on all three windows that we just opened.



Step 3: (Designed for Windows 10) Click on the Windows search bar, type "Task Scheduler", and press
'Enter'. When the system prompts you to allow access to "modify the system", click "Yes". Then, click
on "Create Basic Task...", on the 'Name' field, put "YTAutoDownloader".
*You may add a description, if you wish to*

Click 'Next'. Set the task to start "When I log on". Hit 'Next'. Make sure it's set to "Start a
program". Click 'Next'. On the "Program/script" field, paste the folder you took note of before and add
'\runProgram.bat' to the end.
e.g.: 'C:\YT_Data\runProgram.bat'

Click 'Next' and hit 'Finish'.



Step 4: Now that the program was added to the Windows automated tasks, you must restart the computer
for the changes to take effect. Once you've done that, YOU'RE DONE!

Now all you have to do is add those amazing songs and videos from your favorite composers and
creators and enjoy them when you're offline or out of data, without ever having to worry about
downloading them yourself!

-------------------------------------------------------------------------------------------------------
