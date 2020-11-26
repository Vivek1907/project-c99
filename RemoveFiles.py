import os
import shutil
import time

def main():
    deleted_folder_count = 0
    deleted_file_count = 0
    path = input("Enter the folder path: ")
    days = input("Enter the number of days: ")
    seconds = time.time() - (days*24*3600)
    
    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds >= get_folder_or_file_age(root_folder):
                remove_folder(root_folder)
                deleted_folder_count += 1
                break
            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder, folder)
                    
                    if seconds >= get_folder_or_file_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folder_count += 1
                
                for file in files:
                    file_path = os.path.join(root_folder, file)

                    if seconds >= get_folder_or_file_age(file_path):
                        remove_file(file_path)
                        deleted_file_count += 1
                    
        else:
            if seconds >= get_folder_or_file_age(path):
                remove_file(path)
                deleted_file_count += 1
    
    else:
        print("File or folder not found")


def remove_folder(path):
    if not shutil.rmtree(path):
        print("Path removed succesfully")
    else:
        print("Unable to complete the task")


def remove_file(path):
    if not os.remove(path):
        print("Path removed succesfully")
    else:
        print("Unable to complete the task")


def get_folder_or_file_age(path):
    c_time = os.stat(path).st_ctime
    return c_time


main()
