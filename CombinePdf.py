
# from PyPDF2 import PdfFileWriter, PdfFileReader

# output_Content = PdfFileReader()

# presentaion_pdf_file = open("presentation.pdf", "rb")
# recap_pdf_file = open("recap.pdf", "rb")

# reader_presentation = PdfFileReader(presentaion_pdf_file)
# reader_recap = PdfFileReader(recap_pdf_file)

# print("Number of pages : " + str(reader_recap.getNumPages()))

# output_Content.addPage(reader_presentation.getPage(0))
# for i in range(reader_recap.getNumPages()):
#     output_Content.addPage(reader_recap.getPage(i))

# ouput_file = open("ouput_file.pdf", "wb")
# output_Content.write(ouput_file)

# ouput_file.close()
# presentaion_pdf_file.close()
# recap_pdf_file.close()

from PyPDF2 import PdfWriter, PdfReader

# Utiliser PdfWriter pour créer l'objet de sortie
output_Content = PdfWriter()

presentaion_pdf_file = open("presentation.pdf", "rb")
recap_pdf_file = open("recap.pdf", "rb")

reader_presentation = PdfReader(presentaion_pdf_file)
reader_recap = PdfReader(recap_pdf_file)

output_Content.add_page(reader_presentation.pages[0])
for i in range(len(reader_recap.pages)):
    output_Content.add_page(reader_recap.pages[i])

ouput_file = open("ouput_file.pdf", "wb")
output_Content.write(ouput_file)

ouput_file.close()
presentaion_pdf_file.close()
recap_pdf_file.close()
