from modify_txt import *


def load_spreadsheet(filename):
    """load spreadsheet with all file names

    Args:
        filename (str): name of the txt file we want to add the line to 

    Returns:
        dictionary: dictionary that contains pairs (student ID, file name corresponding to student)
    """
    filename_dict = {}
    add_line(filename)

    # open file
    name_file = open(filename, "r")
    line = name_file.readline()

    file_in_progress = True

    while file_in_progress:
        line_list = line.strip().split(",")
        if line_list[0] not in filename_dict:
            name_of_student_file = "_".join(line_list) + ".pdf"
            filename_dict[line_list[0]] = name_of_student_file

        line = name_file.readline()
        if "This is the end of file" in line:
            file_in_progress = False

    truncate(filename)

    return filename_dict
