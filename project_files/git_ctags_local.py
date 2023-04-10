
# REQUIREMENTS:
#---------------
# GITPYTHON
# UNIVERSAL CTAGS

import os
import git
import shutil
from os import system

# FILE TYPES THAT WILL RUN AS LONG AS SUPPORTED
file_types = ['.py', '.sv', '.v', '.vhd', '.dart']

repo_path = input("Enter the path for your repository: ")

def Git_Repo(path, cleanup = False):
# POTENTIONAL SETUP
    print(path + " is your path. ")
# ACTION STARTS -------------------------
    
    # get current directory
    os.chdir(path)
    current_dir = os.getcwd() 

    # clones git repo for use
    try:
        git.Repo(path)
    except:
        print("Did not download git repo")

    # makes project_files directory
    try:
        os.mkdir(path + "/project_files")
    except:
        print('project_files is already created.')

    # moves files with correct postfix to project_files    
    for root, dir, system_files in os.walk(current_dir):
        for system_file in system_files:
            if system_file.endswith(tuple(file_types)):
                original = os.path.join(root + "/" + str(system_file))                
                target = os.path.join(current_dir + "/project_files/" + str(system_file))
                try:
                    shutil.copyfile(original, target)
                    print("Added source file.")
                except:
                    print("Could not move file")

    # creates the Universal ctags indexed file within your current directory
    try:
        system("uctags -R -f .tags project_files")            
        print(".tags file created successfully! Check in your repository's files ")
    except:
        print("There was an error with ctags")

Git_Repo(repo_path)