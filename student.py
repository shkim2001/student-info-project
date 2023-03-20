import os
import shutil
import fitz
from convert_pdf import *


class Student:
    """Contains all functions used to find, move, convert and merge files for each student
    """

    def __init__(self, student_ID, current_dir, file_name_dict=""):
        """Initialize variables

        Args:
            student_ID (str): student ID of student, owner of documents
            current_dir (str): path of the current directory
        """
        self.student_ID = student_ID
        self.current_dir = current_dir
        self.review_sheet_dir = current_dir + "/review_sheets"
        self.transcript_dir = current_dir + "/transcripts"
        self.degree_audit_dir = current_dir + "/degree_audits"
        self.d_f_form_dir = current_dir + "/d_f_forms"
        self.combined_file_dir = current_dir + "/combined_files/"
        self.student_path = self.combined_file_dir + student_ID
        self.file_name_dict = file_name_dict
        self.file_list = []

    def create_student_dir(self):
        """create indiviudal folders for each student
        """
        if not os.path.exists(self.student_path):
            os.makedirs(self.student_path)
        if not os.path.exists(self.student_path + "/raw"):
            os.makedirs(self.student_path + "/raw")
        if not os.path.exists(self.student_path + "/pdf"):
            os.makedirs(self.student_path + "/pdf")

    def gather_student_files(self):
        """search for files that belong to student ID, convert them to pdf
        """
        self.file_list = os.listdir(self.student_path)
        directory_list = [self.review_sheet_dir,
                          self.transcript_dir, self.degree_audit_dir]

        # loop through the three directories
        for directory in directory_list:
            # if there exists a file in the directory that corresponds to the student ID
            for file in os.listdir(directory):
                if file[:7] == self.student_ID:
                    # print progress
                    if directory == self.review_sheet_dir:
                        print("...Converting review sheet")
                    if directory == self.transcript_dir:
                        print("...Converting transcript")
                    if directory == self.degree_audit_dir:
                        print("...Converting degree audit")
                    # convert file to pdf and add to student folder
                    make_pdf(self.student_path + "/raw/" + file)
                    # move converted file to pdf folder
                    shutil.move(self.student_path + "/raw/" + file.split(".")[0] + ".pdf",
                                self.student_path + "/pdf/" + file.split(".")[0] + ".pdf")

        count = 1
        # loop through D-F form folder
        for form in os.listdir(self.d_f_form_dir):
            form_list = form.split()
            # if there exists a file in the directory that corresponds to the student ID
            if form_list[0] == self.student_ID:
                # print progress
                print("...Adding d-f form", str(count))
                filename = self.student_ID + "_4_" + str(count) +"_d_f_form.pdf"
                count += 1
                # copy files to raw and pdf folder of the student
                shutil.copy(self.d_f_form_dir + "/" + form, self.combined_file_dir +
                            "/" + self.student_ID + "/raw/" + filename)
                shutil.copy(self.d_f_form_dir + "/" + form, self.combined_file_dir +
                            "/" + self.student_ID + "/pdf/" + filename)

    def merge_pdf(self):
        """merge all pdf files for each student to one pdf
        """
        final = fitz.open()

        # access all pdf files for individual student
        file_name = self.find_file_name()
        student_folder = self.student_path + "/pdf"
        student_file_list = os.listdir(student_folder)
        student_file_list.sort()

        # merge all files found as pdf
        for pdf in student_file_list:
            with fitz.open(student_folder + "/" + pdf) as merge_file:
                final.insert_pdf(merge_file)

        # save merged pdf
        print("...Merging PDF")
        final.save(self.student_path + "/pdf/" + file_name)

        # move converted file to all folder
        shutil.copy(self.student_path + "/pdf/" + file_name,
                    self.student_path + "/all/" + file_name)
        shutil.move(self.student_path + "/pdf/" + file_name,
                    self.combined_file_dir + "all/" + file_name)

    def find_file_name(self):
        """finds the corresponding file name for the student

        Returns:
            str: merged file name for the student 
        """
        if self.student_ID in self.file_name_dict:
            return self.file_name_dict[self.student_ID]
        else:
            return self.student_ID + ".pdf"
