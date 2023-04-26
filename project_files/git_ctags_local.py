
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

def Git_Repo(path):
# TELLS USER THE PATH
    print(path + " is your path. ")
# ACTION STARTS -------------------------
    
    # GET THE CURRENT DIRECTORY
    os.chdir(path)
    current_dir = os.getcwd() 
    print(current_dir)
    
    # CREATES THE FILE THAT HOLDS ALL FILE PATHS TO BE INDEXED LATER
    list_source_files = open("files.txt", "a+")

    # MOVES FILES WITH THE CORRECT POSTFIX TO THE FILE
    for root, dir, system_files in os.walk(current_dir):
        for system_file in system_files:
            if system_file.endswith(tuple(file_types)):
                original = os.path.join(root + "/" + str(system_file))                                
                try: 
                    list_source_files.write('{0}\n'.format(original))
                    #copy_file.write('{0}/n'.format(original))
                    print("Added source file.")
                except:
                    print("Could not move file")
    list_source_files.close()

    # CREATES THE UNIVERSAL CTAGS INDEXED FILE WITHIN YOUR CURRENT DIRECTORY
    try:
        system("uctags -L files.txt -f .tags")            
    except:
       print("There was an error with ctags")

Git_Repo(repo_path)
