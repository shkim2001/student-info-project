# created by kims3
# 2023-03-16 Carleton College Spring 2023
# Takes in a txt file name with multiple transcripts and creates new txt files that each contain only one individual transcript
# Preserves same txt formatting as original in new files.

# To run, first remove comments in last part of this code file. Then, put this python file and "something.txt" in the same folder and
# enter a command in format "python3 split_transcript_files.py something.txt" at a terminal prompt,
# where "something.txt" is replaced by the actual name of the txt file to split up

import sys
import re
import os
import shutil
from student import *
from modify_txt import *


def split_transcript(filename):
    """split file into individual transcripts and saves them as "student_id_2_transcript.txt" in transcripts folder

    Args:
        filename (str): name of the txt file that contains all transcripts
    """
    # add end pinpoint to text file for us to check end of file
    add_line(filename)

    # open current directory
    current_dir = os.getcwd()
    transcript_path = current_dir + "/transcripts"

    # create folder if not already there
    if not os.path.exists(transcript_path):
        os.makedirs(transcript_path)

    # open txt file with multiple transcripts
    read_transcript_file_to_split = open(filename, "r")
    line = read_transcript_file_to_split.readline()

    # set status as in progress
    file_in_progress = True

    # while current location of line is not end of the file
    while file_in_progress:
        # initialize or reset header_lines for each student and add the first line (which is "Page 1 of 2")
        header_lines = ""
        header_lines += line
        # read two more lines and add them to header_lines
        for _ in range(2):
            line = read_transcript_file_to_split.readline()
            header_lines += line
        # extract student ID from the line
        student_id = re.search("\d{7}", line).group()
        # create and initialize individual txt file for each student and add info in header_lines to created file
        new_file_name = student_id + "_2_transcript.txt"
        write_transcript_file = open(new_file_name, "w")
        write_transcript_file.write(header_lines)
        # move to next line
        line = read_transcript_file_to_split.readline()

        # update created file until we reach a new student, which is when we reach the line with text "Page 1"
        while "Page 1" not in line:
            # if we reach end of file, change status to end of progress, delete the line we added to turn it back to original format, and break out of loop
            if line == "This is the end of file " + filename:
                truncate(filename)
                file_in_progress = False
                break
            # add line to individual transcript
            write_transcript_file.write(line)
            # move on to next line
            line = read_transcript_file_to_split.readline()

        # close finished transcript
        write_transcript_file.close()

        # move it to transcripts folder
        new_dir = os.path.join(current_dir, "transcripts")
        student_dir = current_dir + "/combined_files/" + student_id
        student_file = Student(student_id, current_dir)
        student_file.create_student_dir()
        shutil.copy(current_dir + "/" + new_file_name,
                    student_dir + "/raw/" + new_file_name)
        shutil.move(current_dir + "/" + new_file_name,
                    new_dir + "/" + new_file_name)

        # if status is end of progress, close reading file and break program
        if not file_in_progress:
            read_transcript_file_to_split.close()
            break


# def main():
#     """
#     main program function
#     """
#     # get txt file name from terminal as input
#     transcript_file_to_split = sys.argv[1]
#     # split the file into individual transcripts
#     split_transcript(transcript_file_to_split)

# main()
