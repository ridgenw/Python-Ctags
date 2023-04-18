
# REQUIREMENTS:
#---------------
# GITPYTHON
# UNIVERSAL CTAGS

import os
import shutil
from os import system

# FILE TYPES THAT WILL RUN AS LONG AS SUPPORTED
file_types = ['.sv', '.v', '.vhd']

def Git_Repo(url, cleanup = False):
# POTENTIONAL SETUP

    for root, dir, files2 in os.walk("/Library"):
        if "GitPython" in files2 == False:
            try:
                os.system("pip3 install GitPython")
                import git
                print("Downloaded GitPython with pip3")
            except:
                try:
                    os.system("pip install GitPython")
                    import git
                    print("Downloaded GitPython with pip")
                except:
                    print("Error downloading GitPython... try downloading with your command-line. ")
        else:
            import git
            print('GitPython is already downloaded')
            break

    for root, dir, files1 in os.walk("/usr/local"):
        if "universal-ctags" in files1 == False: #can find universal ctags downlaoded on device
            try:
                system("git clone https://github.com/universal-ctags/ctags.git \n cd ctags \n ./autogen.sh \n ./configure \n make \n sudo make install")
            except:
                print("There was an error downloading universal ctags from GitHub.")
        else:
            print('"ctags" file was previously found.')
            break
           
# ACTION STARTS -------------------------
    
    # get current directory
    os.system("cd ..") 
    python_dir = os.getcwd() 
    print(python_dir + " is the current directory here")
    list_source_files = open("files", "a+")

    # clones git repo for use
    try:
        git.Repo.clone_from(url, python_dir + "/pyrepo")
    except:
        print("Did not download git repo")

    pyrepo_dir = python_dir + "/pyrepo"

    # moves files with correct postfix to project_files    
    for root, dir, system_files in os.walk(pyrepo_dir):
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



Git_Repo('https://github.com/XarkLabs/BenEaterVHDL.git')