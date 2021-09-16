import pyttsx3                                                    # text to speech
import PyPDF2                                                     # a pure-python PDF library capable of splitting, merging together, cropping, and transforming the pages of PDF files
book =open(r'C:\Users\HP\Documents\Big Data-merged.pdf' , 'rb')   #  the mode string, for a binary file.
pdfreader = PyPDF2.PdfFileReader(book)                            # connect the file to pypdf
pages= pdfreader.numPages                                         # count no. of pages
print(pages)                                                      # print pages of pdf


speaker=pyttsx3.init()

for num in range(1,pages):                                        # pdf start from page one to second last pages
    page=pdfreader.getPage(num)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()
