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
have various versions of Python installed on your system). Take note of the folder the program
displays at the first lines of code, you will need it later on...



Step 2: (Designed for Windows 10) Click on the Windows search bar, type "Task Scheduler", and press
'Enter'. When the system prompts you to allow access to "modify the system", click "Yes". Then, click
on "Create Basic Task...", on the 'Name' field, put "YTAutoDownloader".
*You may add a description, if you wish to*

Click 'Next'. Set the task to start "When I log on". Hit 'Next'. Make sure it's set to "Start a
program". Click 'Next'. On the "Program/script" field, paste the folder you took note of before and add
'\runProgram.bat' to the end.
e.g.: 'C:\YT_Data\runProgram.bat'

Click 'Next' and hit 'Finish'.


Step 3: Now that the program was added to the Windows automated tasks, you must restart the computer
for the changes to take effect. Once you've done that, YOU'RE DONE!

Now all you have to do is add those amazing songs and videos from your favorite composers and
creators and enjoy them when you're offline or out of data, without ever having to worry about
downloading them yourself!

-------------------------------------------------------------------------------------------------------
