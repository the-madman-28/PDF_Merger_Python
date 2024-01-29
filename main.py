import PyPDF2

filess = ["name1.pdf","name2.pdf"]
merger = PyPDF2.PdfMerger()
for filename in filess:
    filee = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(filee)
    merger.append(pdfReader)
filee.close()
merger.write('newpdf.pdf')