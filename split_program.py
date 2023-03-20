# sample terminal command
# python3 split_program.py review_sheet.txt transcript.txt degree_audit.html file_names.csv

from split_degree_audit_files import *
from split_transcript_files import *
from split_review_files import *
from student import *
from extract_file_name import *

import sys
import os
import time


def split_program():
    """main program function
    """
    start_time = time.time()
    # --------------------------------------------
    # 1. splitting all files into individual files
    current_dir = os.getcwd()
    combined_dir = current_dir + "/combined_files/"
    if not os.path.exists(combined_dir):
        os.makedirs(combined_dir)
        os.makedirs(combined_dir + "all")

    # REVEIW FILES
    # get txt file name from terminal as input
    review_file_to_split = sys.argv[1]
    # split the file into individual transcripts
    split_review(review_file_to_split)

    # TRANSCRIPT
    # get txt file name from terminal as input
    transcript_file_to_split = sys.argv[2]
    # split the file into individual transcripts
    split_transcript(transcript_file_to_split)

    # DEGREE AUDITS
    # get txt file name from terminal as input
    degree_audit_file_to_split = sys.argv[3]
    # split the file into individual transcripts
    split_degree_audit(degree_audit_file_to_split)

    # --------------------------------------------
    # 2. convert individual files into pdf files and merge them into one pdf file
    filecount = 0
    student_id_list = os.listdir(combined_dir)

    # create a dictionary of file names for each student
    name_of_files = sys.argv[4]
    name_of_file_dict = load_spreadsheet(name_of_files)

    # loop through list of student ID and convert/merge files for each of them
    for student_id in student_id_list:
        # if there exists a file that is not a student file, pass
        if re.search("\d{7}", student_id) is None:
            pass
        else:
            # print progress
            filecount += 1
            print("Converting file", filecount, "for student", student_id)
            student_path = combined_dir + "/" + student_id

            # if there does not exists an all folder for the student, create one
            if not os.path.exists(student_path + "/all"):
                os.makedirs(student_path + "/all")

            # gather/convert/merge files for each student
            temp_student = Student(student_id, current_dir, name_of_file_dict)
            temp_student.gather_student_files()
            temp_student.merge_pdf()

    elapsed_time = time.time() - start_time
    print("___________PROGRAM RAN___________")
    print("CREATED", filecount, "FILES")
    print('EXECUTION TIME:', time.strftime(
        "%H:%M:%S", time.gmtime(elapsed_time)))


split_program()
