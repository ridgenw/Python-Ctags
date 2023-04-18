
# REQUIREMENTS:
#---------------
# GITPYTHON
# UNIVERSAL CTAGS

import os
import git
from os import system

# FILE TYPES THAT WILL RUN AS LONG AS SUPPORTED
file_types = ['.v', '.sv', '.vhd']

# USER INPUTS
repo_path = input("Enter the path to your repository: ")
removeFile= input("Would you like to keep a copy of all indexed files? y/n: ")

def Git_Repo(path, removeFile):
# TELLS USER THE PATH
    print(path + " is your path. ")
# ACTION STARTS -------------------------
    
    # GET THE CURRENT DIRECTORY
    os.chdir(path)
    current_dir = os.getcwd() 
    
    # CREATES THE FILE THAT HOLDS ALL FILE PATHS TO BE INDEXED LATER
    list_source_files = open("files", "a+")

    try:
        git.Repo(path)
    except:
        print("Did not download git repo")

    # MOVES FILES WITH THE CORRECT POSTFIX TO THE FILE
    for root, dir, system_files in os.walk(current_dir):
        for system_file in system_files:
            if system_file.endswith(tuple(file_types)):
                original = os.path.join(root + "/" + str(system_file))                                
                try: 
                    list_source_files.write('{0}\n'.format(original))
                    print("Added source file.")
                except:
                    print("Could not move file")

    # CREATES THE UNIVERSAL CTAGS INDEXED FILE WITHIN YOUR CURRENT DIRECTORY
    try:
        system("uctags -L files -f .tags")            
    except:
       print("There was an error with ctags")

    if removeFile == "n" or "N":
        os.remove("files")
    

Git_Repo(repo_path, removeFile)
