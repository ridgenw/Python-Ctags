import shutil
import os


def delete(path):
    try:
        try:
            shutil.rmtree(path + "/pyrepo")
        except:
            print(os.getcwd())
        try:
            shutil.rmtree(path + "/project_files")
        except:
            print("Couldn't remove the pyrepo_files")
    except OSError as e:
        print(e.strerror)


delete("/Users/ridgewilliams/Developer/VSCode/Python")