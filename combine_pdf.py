import os
import fitz
import re
import shutil

class Combine_pdf():
    def __init__(self, original, student_path, student):
        self.original_path = original
        self.student_path = student_path
        self.student = student
        self.directory = os.getcwd() + "/combined_files"
        
    # combine all files in each student folder as pdf
    def merge_pdf(self):        
        final = fitz.open()
        
        filename = self.student + ".pdf"
        student_folder = self.student_path + "/pdf"
        student_file_list = os.listdir(student_folder)
        student_file_list.sort()
        if not os.path.exists(self.student_path + "/all"):
            os.makedirs(self.student_path + "/all")
    
        for pdf in student_file_list:
            with fitz.open(student_folder + "/" + pdf) as merge_file:
                final.insert_pdf(merge_file)
        
        final.save(self.student_path + "/pdf/" + filename)
        
        # move converted file to all folder
        shutil.copy(self.student_path + "/pdf/" + filename,
                    self.student_path + "/all/" + filename)
        shutil.move(self.student_path + "/pdf/" + filename,
                    self.original_path + "/all/" + filename)
    
# def move_pdf(self):
#     student_id_list = os.listdir(self.directory)
#     if not os.path.exists(self.directory + "/all"):
#         os.makedirs(self.directory + "/all")
        
    # for student in student_id_list:
    #     if re.search("\d{7}",student) is None or len(student) == 11:
    #         pass
    #     else:
    #         print("Combining file for student", student)
    #         student_path = self.directory + "/" + student
    #         merge_student = self.merge_pdf(self.directory, student_path, student)
    #         merge_student.merge_pdf()