"""
This program will take a multiple page PDF, and break it on the page line
into multiple PFD files.

Program compiled from Stack Overflow and Automate the Boring Stuff
with Python by Al Sweigart.
"""


import os
from PyPDF2 import PdfFileReader, PdfFileWriter

#merged.pdf is the file to be broken into multiple files
#further development incorporate some sort of input
inputpdf = PdfFileReader(open("merged.pdf", 'rb'))

for i in range(inputpdf.numPages):
	output = PdfFileWriter()
	output.addPage(inputpdf.getPage(i))
	with open("result-page%s.pdf" % i, "wb") as outputStream:
		output.write(outputStream)

		