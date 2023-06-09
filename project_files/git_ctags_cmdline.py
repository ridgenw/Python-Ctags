
# REQUIREMENTS:
#---------------
# GITPYTHON
# UNIVERSAL CTAGS

import os
import shutil
from os import system
import git

# FILE TYPES THAT WILL RUN AS LONG AS SUPPORTED
file_types = [".py", ".v", ".vhd", ".sv"]

URL = input("Paste or type GitHub URL: ")

def Git_Repo(url, cleanup = False):
# POTENTIONAL SETUP

           
# ACTION STARTS -------------------------
    
    # get current directory
    os.system("cd ..") 
    python_dir = os.getcwd() 
    print(python_dir + " is the current directory here")

    # clones git repo for use
    try:
        git.Repo.clone_from(url, python_dir + "/pyrepo")
    except:
        print("Did not download git repo")

    # makes project_files directory
    try:
        os.mkdir(python_dir + "/project_files")
        print("directory made")
    except:
        print('Pyrepo file is already created.')

    pyrepo_dir = python_dir + "/pyrepo"

    # moves files with correct postfix to project_files    
    for root, dir, system_files in os.walk(pyrepo_dir):
        for system_file in system_files:
            if system_file.endswith(tuple(file_types)):
                try:
                    shutil.move(os.path.join(root + "/" + str(system_file)), os.path.join(python_dir + "/project_files"))
                    print("Added files to pyrepo file")
                except:
                    print("Could not move files")

    # creates the Universal ctags indexed file within your current directory
    try:
        system("uctags -R -f tags . project_files")            
        print('Utags file created successfully')
    except:
        print("There was an error with ctags")

    # optionally removes the old git clone
    if cleanup == True:
        path = python_dir
        try:
            shutil.rmtree(path + "/pyrepo")
        except:
            print(os.getcwd())

        try:
            shutil.rmtree(path + "/project_files")
        except:
            print("Couldn't remove the pyrepo_files")



Git_Repo(URL)