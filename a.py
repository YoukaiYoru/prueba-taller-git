# read a pdf file and extract text from it
import PyPDF2

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(pdf.getNumPages()):
            text += pdf.getPage(page_num).extract_text()
    return text

# create an object of the class and call the method to read the pdf file
pdf_reader = read_pdf('sample.pdf')
class A:
    def __init__(self):
        self.text = pdf_reader

    def get_text(self):
        return self.text

def multi(int1, int2):
    return int1 * int2

print(multi(1, 2))
