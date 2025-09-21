import PyPDF2

wordies = ""

with open('C:/Users/jurko/Desktop/Books/Other/Business/PrinciplesofManagement.pdf', 'rb') as f:
    pdfReader = PyPDF2.PdfReader(f)

    for i in range(16,20):
        pageObj = pdfReader.pages[i]
        print(pageObj.extract_text())

