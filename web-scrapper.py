##################################################### 
# Objective: To create a web scrapper that uses data 
# from an already opened brower tab in firefox to 
# take the data for the mp4 of a panapto recording
# and download it automatically to a given directory.
# ###################################################

###################################################################################
# Goals:
#   In target directory that contains file that is pre-parsed
#   and awaiting processing.
#   Program will ask for file name
#   Program will parse up the links that are iterated through by some form of list.
#       [[link, title],[link, title],[link, title],[link, title]]
#   Display things are working by showing the numbers within the title
#   Upload to github to show progress
###################################################################################
#  Command Line Program Syntax: python web-scrapper.py filename.txt
#########################################################################

import sys
import os.path




#################
# File format
# URL,file_name
# foo,bar
#################

def main():
    file_name = sys.argv[1] #something.txt
    file_reader = open_file(file_name) #inside something.txt
    file_lines = file_reader.readlines() #Returns string array of each line in the file.
    file_lines = strip_new_lines(file_lines)


def open_file(file_name):
    '''Returns an open file Object from input file name'''
    return open(file_name)


def strip_new_lines(file_lines):
    '''Returns array of sanitized strings (removes carriage-returns)'''



    returned_array = [] #this will contain the stripped down strings from our input

    # Reading things in order
    for line in file_lines:
        temp = line.strip()
        returned_array.append(temp) #Put the newly stripped string back into place


    return returned_array



main()
