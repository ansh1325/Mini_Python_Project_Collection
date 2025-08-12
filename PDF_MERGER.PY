import PyPDF2
pdf_files=["visible.pdf","demo.pdf"]
merger=PyPDF2.PdfMerger()
for files in pdf_files:
    file=open(files,'rb')
    readfile=PyPDF2.PdfReader(file)
    merger.append(readfile)
file.close()
merger.write("Merged.pdf")