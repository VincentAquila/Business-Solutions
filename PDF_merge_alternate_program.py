"""
This code will merge multiple PDFs into one PDF file

Why not use a third party app?  Sensitive documents shouldn't be uploaded to third part apps.
"""

import os
from PyPDF2 import PdfFileMerger

#the variable 'path' is the folder that contains the two separate PDFs that are to be merged
path = '/Users/nameOfHomeDirectory/Folder/SubFolder2/SubFolder3 .../'

#the variable 'pdf_files' is a list that shows the two files that are to be merged
pdf_files = ['document1.pdf', 'document2.pdf']

#merger is the object
merger = PdfFileMerger()
for files in pdf_files:
    merger.append(path + files)

#this keeps from over-writing an existing file - if this file exists, it won't proceed with the code
if not os.path.exists(path + 'merged.pdf'):
    #write the information into a new file (called 'merged.pdf')
    merger.write(path + 'merged.pdf')

#closes all the temp files created by the above functions
merger.close()