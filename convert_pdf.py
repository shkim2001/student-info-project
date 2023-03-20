from pyhtml2pdf import converter
from fpdf import *

def make_pdf(filepath):
    """Convert html and txt files into pdf format

    Args:
        filepath (str): path of file that we want to convert to pdf
    """
    # if file is an html file
    if filepath.endswith(".html"):
        converter.convert(f'file:///{filepath}', filepath[:-5] + ".pdf")

    # if file is a txt file
    if filepath.endswith(".txt"):
        file = open(filepath, "r")
        pdf = FPDF("P")
        pdf.add_page()
        pdf.set_font('courier', size=11)

        for line in file:
            pdf.cell(200, 4, txt=line, ln=1)

        pdf.output(filepath[:-4] + ".pdf", "F")
