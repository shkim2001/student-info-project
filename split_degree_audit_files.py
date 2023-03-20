# created by misplonj
# 2022-09-16 Carleton College Fall 2022
# Modified 2023-03-18 by kims3
# - fixed naming of output files to be in format "studentID_3_degree_audits.html"
# - fixed that the files are saved in a folder called "degree_audits"

# Takes in a html file name with multiple degree audits and creates new html files that each contain only one degree audit
# Preserves same html formatting as original in new files.
# To run, first remove comments in last part of this code file. Then, put this python file and "something.txt" in the same folder 
# and enter something like "python3 split_degree_audit_html_files.py something.html" at a terminal prompt,
# where "something.html" is replaced by the actual name of the html file to split up

import sys
import os
import shutil
from student import *


def split_degree_audit(filename):
    """split file into individual degree audits and saves them as "student_id_3_degree_audit.html" in degree_audit folder

    Args:
        filename (str): name of the html file that contains all degree audits
    """
    # open current directory
    current_dir = os.getcwd()
    degree_audit_folder_path = current_dir + "/degree_audits"

    # create folder if not already there
    if not os.path.exists(degree_audit_folder_path):
        os.makedirs(degree_audit_folder_path)

    # Initializing header and footer lines that are shared between all split degree audit files (such as styling)
    footer_lines = ""
    header_lines = ""

    # Read through file until footer lines are reached, then set footer_lines to whatever follows
    file_reading_to_get_footer = open(filename, "r")
    line = file_reading_to_get_footer.readline()
    while "/body" not in line:
        line = file_reading_to_get_footer.readline()
    footer_lines += line
    while line:
        line = file_reading_to_get_footer.readline()
        footer_lines += line
    file_reading_to_get_footer.close()

    file_to_split_opened = open(filename, "r")

    # Read in header lines until end of styling is reached - end marked by "</style>" tag
    line = file_to_split_opened.readline()
    while "</style>" not in line:
        header_lines += line
        line = file_to_split_opened.readline()
    header_lines += line

    # Don't want to include index table, so loop until first student name anchor is encountered
    while "<a name" not in line:
        line = file_to_split_opened.readline()

    # Loop through rest of document until footer lines reached, writing to new degree audit html file everytime a new student id is encountered
    degree_audit_contents = ""
    while "</body>" not in line:
        degree_audit_contents = line

        # This way of getting the student id relies on student id lines having formatting like this: <a name="1234567UNDC"></a>
        student_identifier_extended = line.split("\"")[1]

        # Remove any trailing information beyond 7 digit student id
        student_identifier = student_identifier_extended[:7]

        # Gather degree audit contents until start of next degree audit or end of degree audit contents
        line = file_to_split_opened.readline()
        while ("<a name" not in line and "</body>" not in line):
            degree_audit_contents += line
            line = file_to_split_opened.readline()

        # Write out student's degree audit to html file with their student id as filename
        new_file_name = student_identifier + "_3_degree_audit.html"
        single_degree_audit_file = open(new_file_name, "w")
        single_degree_audit_file.write(
            header_lines + degree_audit_contents + footer_lines)
        single_degree_audit_file.close()

        # move it to degree audits folder
        new_dir = os.path.join(current_dir, "degree_audits")
        student_dir = current_dir + "/combined_files/" + student_identifier
        student_file = Student(student_identifier, current_dir)
        student_file.create_student_dir()
        shutil.copy(current_dir + "/" + new_file_name, student_dir + "/raw/" + new_file_name)
        shutil.move(current_dir + "/" + new_file_name,
                    new_dir + "/" + new_file_name)

    file_to_split_opened.close()


# def main():
#     degree_audit_file_to_split = sys.argv[1]
#     split_degree_audit(degree_audit_file_to_split)

# main()
