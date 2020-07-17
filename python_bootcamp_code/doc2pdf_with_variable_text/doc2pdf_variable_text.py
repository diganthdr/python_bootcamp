#Input is a docx file with some kind of template, for document generation,
#User provides some text to replace the text in template.
#Output is a pdf file 

#This is simple script withour error handling. Use this to craft them on top of this

from docx2pdf import convert
from docx import Document

#This is variable text, can be read from settings file or any other inputs.
input_map = {
    "<name>" : "Soumya",
    "<policy>" : "ABC4571010",
    "<date>" : "01 January 2021",
    "<discount>" : "2",
    "<link>" : "www.paymentlink.com"
}

#Globals
import sys
import os

BASE_DIR = os.getcwd()
template = os.path.join( BASE_DIR, "input_policy_test_template.docx")
TEMP_REPLACED_DOC = os.path.join(BASE_DIR, "_temp.docx")
PDF_FILE_NAME = os.path.join( BASE_DIR, "output_policy_reminder.pdf")

def replace_words_in_document(input_map, template):
    document = Document(template)

    for p in document.paragraphs:
        inline = p.runs
        for in_text in inline:
            text = in_text.text
            for key,val in input_map.items():
                if key in text: 
                    text=text.replace(key,val)
                    in_text.text = text
    document.save(TEMP_REPLACED_DOC)
    return True #for now


def make_custom_report(input_map, template):

    #fill the template:
    replace_words_in_document(input_map, template)

    #convert to pdf.
    convert(TEMP_REPLACED_DOC, PDF_FILE_NAME)

#start here
make_custom_report(input_map, template)



#--------------------------------------------
# relies on ms office that is installed in Office package.
#--------------------------------------------
#refs: 
#https://stackoverflow.com/questions/34779724/python-docx-replace-string-in-paragraph-while-keeping-style
