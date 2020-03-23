import os
from PyPDF2 import PdfFileReader
 
os.chdir("/home/meco/Python/Desde0")
f = "CV_KatherinPerez.pdf"
 
pdf= PdfFileReader(f)
 
with open("text.txt", "w") as text:
    for page in pdf.pages:
        text.write(page.extractText())