# bib2csv
This Python module combines bibliography files into one excel file.
Use this module when you have several .bib files that you want to 
combine in a simple, readable excel file.
Before you use this module, make sure you have already installed the following
external modules:
bibtexparser, pandas, openpyxl

PROCEDURE FOR MAKING THIS MODULE WORK:
1. Put your .bib files in one folder ("infolder")
2. Designate another folder to contain the output of this module ("outfolder")
3. Change the object values in lines 8-11
4. Run this module
Your output will be one csv file and one excel file, which contain
the most relevant bits of information for all the entries in your
bib files.
Note: you can change which variables this code extracts from the bib
files by changing the object "cols".

FUTURE CHANGES:
- Include a column for making decisions like in the Training files
- 
