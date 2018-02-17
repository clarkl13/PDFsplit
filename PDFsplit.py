#Splits a large pdf into small pdfs.  Renames the smaller pdf based on text found in the pdf.

import PyPDF2
import re
import os

filename = '26R.pdf'

# open the large pdf in read mode
open_pdf = PyPDF2.PdfFileReader(open(filename, 'rb'))
output = PyPDF2.PdfFileWriter()
filename = None

# for each page in the pdf get page and extract text
for i in range(open_pdf.numPages):
    page_obj = open_pdf.getPage(i)
    pdf_text = page_obj.extractText()

    # use regex to find new pdf name
    pad_name = re.findall('waste generation and storage.*\n (.*)-', pdf_text, re.MULTILINE)
    pad_name = " ".join(pad_name)

    #if new pdf contains new filename, create new file and write pages belonging to that file into the new pdf
    if len(pad_name) > 0:
        if filename != None:
            with open(filename, "wb") as output_pdf:
                output.write(output_pdf)
        filename = pad_name + "_802" + "_26R" + ".pdf"
        output = PyPDF2.PdfFileWriter()
        output.addPage(page_obj)

    else:
        output.addPage(page_obj)

#writes the last page of the pdf to the file
with open (filename, "wb") as output_pdf:
    output.write(output_pdf)





