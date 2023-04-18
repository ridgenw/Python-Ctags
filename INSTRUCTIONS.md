These programs take a git repository and generate an indexed universal ctags file, considering the source files are written in a language supported by universal ctags. It will also create a file called "files" that contains all files that ctags actually indexed. These should be all your source files. You will find all Python programs in the "project_files" folder.

# GIT_CTAGS_CMDLINE ==>
You can forget about this file for now, it is not important

# GIT_CTAGS_LOCAL ==>
This is the program you will want to use if your repositry is on your local drive. You will be asked to input a string of the path to the repository you want to use.

# GIT_CTAGS_VSC ==>
This is the program to use if you have a URL from GitHub. You will have to enter the URL into the program itself.

# RESTART_VSC ==>
This program is also not very important, it simply clears out the "project_files" folder.


TIPS FOR USE ------

* The file_types variable hold all the types of files to look for when creating the ctags file. Just type whatever additions you need depending on the language of the source files.

* You can configure this program to be ran in your command line interface. I'm sure you can figure that out, but if not I know how to do it and would love to help.
