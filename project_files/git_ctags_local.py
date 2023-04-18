
# REQUIREMENTS:
#---------------
# GITPYTHON
# UNIVERSAL CTAGS

import os
import git
import shutil
from os import system

# FILE TYPES THAT WILL RUN AS LONG AS SUPPORTED
file_types = ['.v', '.sv', '.vhd']

repo_path = input("Enter the path to your repository: ")
removeFile= input("Would you like to keep a copy of all indexed files? y/n: ")

def Git_Repo(path, removeFile):
# POTENTIONAL SETUP
    print(path + " is your path. ")
# ACTION STARTS -------------------------
    
    # get current directory
    os.chdir(path)
    current_dir = os.getcwd() 
    list_source_files = open("files", "a+")

    # clones git repo for use
    try:
        git.Repo(path)
    except:
        print("Did not download git repo")

    # makes project_files directory

    # moves files with correct postfix to project_files    
    for root, dir, system_files in os.walk(current_dir):
        for system_file in system_files:
            if system_file.endswith(tuple(file_types)):
                original = os.path.join(root + "/" + str(system_file))                                
                try: 
                    list_source_files.write('{0}\n'.format(original))
                    print("Added source file.")
                except:
                    print("Could not move file")

    # creates the Universal ctags indexed file within your current directory
    list_source_files.close()
    try:
        system("uctags -L files -f .tags")            
    except:
       print("There was an error with ctags")

    if removeFile == "n" or "N":
        os.remove("files")
    

Git_Repo(repo_path, removeFile)

# open a new file that holds the complete paths of all allowed files, 
# then run ctags on that file to preserve locations.