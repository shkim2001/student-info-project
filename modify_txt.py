def add_line(filename):
    """add line at the end of text file

    Args:
        filename (str): name of the txt file we want to add the line to 
    """
    read_transcript_file_to_split = open(filename, "a")
    read_transcript_file_to_split.write(
        "\nThis is the end of file " + filename)
    read_transcript_file_to_split.close()


def truncate(filename):
    """remove line from the end of text file

    Args:
        filename (str): name of the txt file we want to remove the line of 
    """
    file_to_truncate = open(filename, "r")
    read_file_to_truncate = file_to_truncate.read()
    file_to_truncate.close()
    split_file_to_truncate = read_file_to_truncate.split("\n")
    join_file_to_truncate = "\n".join(split_file_to_truncate[:-1])
    file_to_truncate = open(filename, "w+")
    for i in range(len(join_file_to_truncate)):
        file_to_truncate.write(join_file_to_truncate[i])
    file_to_truncate.close()
