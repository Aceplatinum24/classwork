# ## 1
# ## Try this. 
# ## It won't display anything to the screen -- rather, it creates a file.
# ## Try to find the file it created.
# f = open("something_very_unique_file.txt", "w", encoding="utf-8")
# f.write("Here are some words.\n")
# f.write("More words.\n")
# f.close()
# ## Memo: Within the 'open()' command, the "w" invokes the "write" mode, 
# ##       which creates a new file if the specified file does not exist,
# ##       or overwrite the contents of the file if it does exist.


# ## 2
# ## Using Python,
# ## Open the file my_thoughts.txt.
# ## Write at least 10 separate lines in it.
# ## Close the file.


# ## 3
# ## Using Python,
# ## Ask the user for name and age.
# ## Open a file called person_info.txt.
# ## Write in that file, "___ is ___ years old" (with the name and age filled in).
# ## Close the file.


# ## 4
# ## Try this.
# f = open("something_very_unique_file.txt", "r", encoding="utf-8")
# contents = f.read()
# print(contents)
# f.close()


# ## 5
# ## When opening a file in Python, if you don't specify a mode, 
# ## Python will default to 'read' mode ('r'). 
# ## So, this is equivalent to the previous example:
# f = open("something_very_unique_file.txt", encoding="utf-8")
# contents = f.read()
# print(contents)
# f.close()

# ## 6
# ## Another example of writing to a file.  
# ## If the file exists, it will be over-written.
# f = open("yay_new_file.txt", "w", encoding="utf-8")
# f.write("Here are some words for you.\n")
# f.close()

# ## Now let's read the file
# f = open("yay_new_file.txt", encoding="utf-8")
# contents = f.read()
# print(contents)
# f.close()

# ## Now write into the file again but with different text
# f = open("yay_new_file.txt", "w", encoding="utf-8")
# f.write("I overwrote those words.\n")
# f.close()

# ## Now let's read the file again for proof that the 
# ## original text was overwritten.
# f = open("yay_new_file.txt", encoding="utf-8")
# contents = f.read()
# print(contents)
# f.close()


# ## 7
# ## If you want to be more cautious, you can use "x" instead of "w", 
# ## which will give an error if the file already exists 
# ## (rather than overwriting it).
# f = open("yay_new_file.txt", "x", encoding="utf-8")
# f.write("Words to put in the file\n")
# f.close()


# ## 8
# ## If you want to write at the end of a file ("append"), you can use "a".
# f = open("yay_new_file.txt", "a", encoding="utf-8")
# f.write("This will write at the end of an existing file.\n")
# f.close()
