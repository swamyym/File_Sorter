# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 00:46:01 2017

@author: swamy
"""

import os

def file_sort(folder_dest,folder_source,file_type):
    try:
        for file in os.listdir(folder_source):

            if os.path.isdir(os.path.join(folder_source,file)):
                file_sort(folder_dest,os.path.join(folder_source,file),file_type)
            if file.endswith(file_type):
                try:
                    os.rename(os.path.join(folder_source,file),os.path.join(folder_dest,file))
                except Exception as e:
                    print("Error in replaceing the file. ",e)
    except Exception as e:
        print("Error in file Location. ",e)

folder_source =  input("Enter Source Path:")
folder_dest= input("Enter Destination path:")
file_type = input("Enter File type:")

file_sort(folder_dest,folder_source,file_type)
print(os.getcwd())