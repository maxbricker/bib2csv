import bibtexparser
import pandas as pd
import os
import openpyxl

# CHANGE THE VALUES OF THESE OBJECTS TO MATCH YOUR OWN
# DESKTOP SETTINGS AND YOUR DESIRED NAME FOR THE OUTPUT FILE
infolder = "/Users/maxbricker/Documents/3ie/bibfiles"
outfolder = "/Users/maxbricker/Documents/3ie/excelfiles"
outsheet = outfolder + "/" + "sussex_ids.csv"
outcel = outfolder + "/" + "sussex ids.xlsx"

db = pd.DataFrame()
for (root, dir, files) in os.walk(infolder):
    for f in files:
        name, ext = os.path.splitext(f)
        if ext == ".bib":
            path = os.path.join(root, f)
            with open(path) as bibpath:
                bib_db = bibtexparser.load(bibpath)
                x = pd.DataFrame(bib_db.entries)
                db = db.append(x)
cols = ['author',
        'issn',
        'isbn',
        'title',
        'year',
        'abstract']
db.to_csv(outsheet,
          columns=cols,
          index=False)
db.to_excel(outcel,
            columns=cols,
            index=False)
