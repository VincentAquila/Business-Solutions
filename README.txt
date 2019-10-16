How to run this program:

In the same directory, store the Python program PDF_multiple_merge.py and the separate PDF files that are to be merged into one PDF file.

Before running this program, be sure to delete any current program result from previous program runs, or else the program will throw errors.

The program for loops (using a list comprehension) through any file with a .pdf extension in the specified directory, grabs it, then merges the separate PDFs together, and will output a new file called "result.pdf".

The PDF_merge_alternate_program.py is a longer and probably less 'Pythonic' version, and it requires the user to manually enter the file names in line 14.



Python libraries:

using Python 3.6

os

PyPDF2 - this isn't part of the Python standard library, to load to your machine use:

	pip install PyPDF2



Background:

I work as a management analyst and have been studying computer science/programming.  My employer does not have the security permissions to deploy python to its network, so I resort to moving files to my personal computer and working on them there (minus anything with privacy information or security matters).  Out of the 4,000 some employees in my organization, there are only a few individuals who have the Adobe Pro seat (which is expensive), which can manipulate PDFs.  Everyone else is left to find other resourceful means, such as wasting time by standing over a printer, printing separate documents, then rescanning them as a whole to accomplish what this program can do.  Finding the one person who has the Adobe Pro seat on their machine, waiting for their response to assist, is a wasteful use of time and printer materials (which are expensive).  So I resort to this program to manipulate PDFs.  My supervisor was enthralled with the productivity/cost savings.  We were faced with having to combine some 25 separate documents into one PDF, and this program was a solution (again, for generalized forms, nothing with privacy information nor security matters).  I am not sure how Adobe will view their proprietary software being sidelined by an open source programming language.  That is a matter for the legal department.  



Resources:

YouTube - there are many videos on PDF merges and the PyPDF2 Python library.  Users will need to import the PyPDF2 library to their machine, as it is not part of the Python standard library.


Automate the Boring Stuff With Python by Al Sweigart.  See chapter 13: Working with PDF and Word Documents.  This is an excellent resource for beginners and experienced Python developers.  This book is free, and can be downloaded.
