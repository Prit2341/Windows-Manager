import os
from pdf2docx import Converter

def convert_pdf_to_docx(pdf_path, output_path):
    try:
        cv = Converter(pdf_path)
        cv.convert(output_path, start=0, end=None)
        cv.close()
        return True
    except Exception as e:
        print(f"An error occurred during conversion: {str(e)}")
        return False

if __name__ == "__main__":
    pdf_path = input("Enter the PDF file location: ")
    output_path = input("Enter the output DOCX file location: ")

    if os.path.isfile(pdf_path):
        if convert_pdf_to_docx(pdf_path, output_path):
            print("PDF to DOCX conversion completed successfully!")
        else:
            print("An error occurred during conversion.")
    else:
        print("PDF file not found at the specified location.")
