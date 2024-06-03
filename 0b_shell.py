## 1 
## - Using the Graphical User Interface (GUI) file browser, open the folder "term_example_files" on the Desktop.
##   This folder should have been created by the initial setup script that you ran in the Preliminaries lesson.
## - Open the files and folders to see what is in them.


## 2
## Now that we've explored the contents using the graphical interface with which you are familiar,
##     we're going to explore the folder structure and files using the CLI (Command Line Interface),
##     a.k.a., the Terminal program.
## First, open an instance of the Terminal by one of several methods:
##     (a) In a GUI files browser, in the right window pane, right-click on white space and select "Open in Terminal".
##     (b) On the computer's Desktop, right-click and select "Open in Terminal".
##     (c) Press the "super" button & begin typing "terminal".  When the appropriate icon appears, click on it.
##     (NOTE:  The "super" button appears as a square formed of small squares, located in the lower left corner of
##      the Ubuntu Desktop. On your keyboard, it may look like a flying window, or a flapping flag having 4 sections.) 
## NOTE: As you type commands or names of folders or files in the CLI (the Terminal),
##     you can SAVE TIME by pressing the Tab key to autofill the rest of a command or name.
##     For example, you can type cd ~/Des (the first three letters of "Desktop") and then press Tab, and the OS
##     will add the remainder of that folder name. If this autofill feature is not working, let an instructor know.
## Now, run these commands:  (Remember, press the Enter key after each line.)
cd ~
pwd
## What happened?
## What does the tilde ~ represent?
## Do this.
cd Desktop
pwd
cd term_example_files
pwd
cd animals
pwd
## Notice the change in your location when you run pwd.
## We can do these commands seperately like the example above or together like the example below.
cd ~
cd Desktop/term_example_files/animals/
## Lets add another command
ls
## What happened?

