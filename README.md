# Student Information Project

## Abstract

This program was created for the Carleton College registrar's office, in purpose of splitting student documents and parsing them into one pdf file. This README is written for users assuming that the users already have an IDE(Integrated Development Environment) like [Visual Studio Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/) and python3 installed in their computers.
_________________

## Table of Contents

- [Description](#description)
- [Files](#files)
- [Instruction](#instruction)
- [Credits](#credits)
_________________

## Description

This project was made to do the following:
* Split a text file with multiple academic review sheets into text files that contain academic review sheets.
* Split a text file with multiple transcripts into text files that contain individual transcripts.
* Split a html file with multiple degree audits into html files that contain individual degree audits.
* Convert the individual files into pdf format.
* Merge multiple pdf files for individual students into one pdf file.
* Name the merged pdf file as desired file name.
_________________

## Files

* **modify_txt.py** : add line at and remove line from the end of text file
* **split_reveiw_files.py** : split file into individual review sheets and saves them as "student_id_1_review.txt" in review_sheets folder
* **split_transcript_files.py** : split file into individual transcripts and saves them as "student_id_2_transcript.txt" in transcripts folder
* **split_degree_audit.py** : split file into individual degree audits and saves them as "student_id_3_degree_audit.html" in degree_audit folder
* **convert_pdf.py** : Convert html and txt files into pdf format
* **extract_file_name.py** : Extract file names from spreadsheet
* **student.py** : Find, move, convert, merge, and name files for each student
* **split_program.py** : Main program

_________________

## Instruction

If this is the first time you are downloading or using this program, you may need to download several packages that allow you to convert files into pdf and merge pdfs. The following are the package name, information link, and the command to download the packages.

**pyhtml2pdf**\
Further information about the package can be found [here](https://pypi.org/project/pyhtml2pdf/).
```terminal
python3 -m pip install pyhtml2pdf
```

**FPDF**\
Further information about the package can be found [here](https://pyfpdf.readthedocs.io/en/latest/).
```terminal
python3 -m pip install fpdf
```

**PyMuPDF**\
Further information about the package can be found [here](https://pymupdf.readthedocs.io/en/latest/).
```terminal
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pymupdf
```

After downloading the packages above, you can now use the program by going through the following steps. 

<ol>
  <li>Add five files in the <i>student_info_project</i> folder and rename them like the following:
    <ul>
        <li>a. <b>TXT</b> file named <i>review_sheet.txt</i> that contains the <b>Review Sheets</b>.</li>
        <li>b. <b>TXT</b> file named <i>transcript.txt</i> that contains the <b>Transcripts</b>.</li>
        <li>c. <b>HTML</b> file named <i>degree_audit.html</i> that contains the <b>Degree Audits</b>.</li>
        <li>d. <b>Folder</b> named <i>d_f_forms</i> that contains all D-F Forms.</li>
        <li>e. <b>CSV</b> file named <i>file_names.csv</i> that contains the desired file names for all students.</li>
    </ul>
   </li>
   <li>Open the terminal and run the following command:</li>
</ol>

```terminal
python3 split_program.py review_sheet.txt transcript.txt degree_audit.html file_names.csv
```

After running the program, you will now find four sub-folders newly made in the *student_info_project* folder:

<ol>
  <li><b>review_sheets</b> folder that contains individual review sheets.<br> Files are named in format <i>student_id_1_review.txt</i>.</li>
  <li><b>transcripts</b> folder that contains individual transcripts.<br> Files are named in format <i>student_id_2_transcript.txt</i>.</li>
  <li><b>degree_audits</b> folder that contains individual degree audits.<br> Files are named in format <i>student_id_3_degree_audit.html</i>.</li>
  <li><b>combined_folder</b> folder that contains following folders.
    <ul>
    <li>a. <b>all</b> folder that contains combined pdf files for all students. <br> Files are named in format <i>student_id.pdf</i>.
    <li>b. Folders named by student ID(ones existing in the inputted files) each containing the following:
        <ul>
        <li>i. <b>raw</b> folder that contains all individual documents for each student in their original format.</li>
        <li>ii. <b>pdf</b> folder that contains all individual documents for each student in a pdf format.</li>
        <li>iii. <b>all</b> folder that contains a single pdf file with all documents combined.</li>
        </ul>
    </ul>
  </li>
</ol>

_________________

## Credits

The splitting program for degree audits was provided by misplonj, and was modified during the process of putting this program together.