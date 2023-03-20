# created by kims3
# 2023-03-18 Carleton College Spring 2023
# Looks for corresponding documents for each student and  .

# To run, first remove comments in last part of this code file. Then, put this python file and "something.txt" in the same folder and
# enter a command in format "python3 split_review_files.py something.txt" at a terminal prompt,
# where "something.txt" is replaced by the actual name of the txt file to split up

import os
import shutil
from convert_pdf import *

class Find_match:
    """ 
    Class used to find files for each student and sort them
    """
    def __init__(self, path):
        """ 
        initializing variables used in Find_match class
        Arguments:
            path -- the path of the directory with the files that we want to convert to pdf files (str)
        """
        self.path = path
        self.filesList = []
        self.combined_folder_path = ""
        self.student_folder_path = ""

    def get_all_files_in_directory(self):
        """ 
        get all the names in a folder
        """
        self.filesList = os.listdir(self.path)

    def add_found_file(self, current_dir):
        """ 
        add each file to matching student folder
        Arguments:
            current_dir -- the path of the folder where the file is originally saved (str)
        """
        # initializing count
        count = 1
        # create combined_files folder
        self.combined_folder_path = current_dir + "/combined_files"
        if not os.path.exists(self.combined_folder_path):
            os.makedirs(self.combined_folder_path)

        # access each student ID
        for file in self.filesList:
            # extract student ID from file name
            student_ID = file[:7]
            # if there is no folder for student, create folder and subfolders for student
            self.student_folder_path = self.combined_folder_path + "/" + student_ID
            folder_names = [self.student_folder_path, self.student_folder_path +
                            "/pdf", self.student_folder_path + "/raw"]
            for i in range(3):
                if not os.path.exists(folder_names[i]):
                    os.makedirs(folder_names[i])

            # add each file to student folder
            original_file_path = self.path + "/" + file
            print("Move files for student", student_ID)
            shutil.copy(original_file_path,
                        self.student_folder_path + "/raw/" + file)

            # # print message that shows the progress
            # print("Converting file", count, file)
            # count += 1
            
            # # convert file to pdf and add to student folder
            # make_pdf(self.student_folder_path + "/raw/" + file)

            # # move converted file to pdf folder
            # shutil.move(self.student_folder_path + "/raw/" + file.split(".")[0] + ".pdf",
            #             self.student_folder_path + "/pdf/" + file.split(".")[0] + ".pdf")

# def main():
#     # open current directory
#     current_dir = os.getcwd()

#     # convert review sheet files
#     review_sheet_dir = current_dir + "/review_sheets"
#     change_review_sheet = Find_match(review_sheet_dir)
#     change_review_sheet.get_all_files_in_directory()
#     change_review_sheet.add_found_file(current_dir)

#     # convert transcript files
#     transcript_dir = current_dir + "/transcripts"
#     change_transcript = Find_match(transcript_dir)
#     change_transcript.get_all_files_in_directory()
#     change_transcript.add_found_file(current_dir)

#     # convert degree audit files
#     degree_audit_dir = current_dir + "/degree_audits"
#     change_degree_audit = Find_match(degree_audit_dir)
#     change_degree_audit.get_all_files_in_directory()
#     change_degree_audit.add_found_file(current_dir)


# main()
