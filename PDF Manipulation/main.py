#This is basic pdf merging, good ones will be created later
from pypdf import PdfWriter
import os

pdf_files = []
files = os.listdir("PDF Manipulation")
merger = PdfWriter()
i = 0
for file in files:
    if file.endswith('.pdf'):
        pdf_files.append(f"PDF Manipulation\{file}")

for pdf in pdf_files:
    merger.append(pdf)
merger.write(f'PDF Manipulation\mergedpdfnew.pdf')
merger.close()