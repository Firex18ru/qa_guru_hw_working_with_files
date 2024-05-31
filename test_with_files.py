from zipfile import ZipFile
from pypdf import PdfReader
import csv
import zipfile

def test_pdf():
    with ZipFile("resources/folder.zip", "r") as folder_zip:
        with folder_zip.open("tmp/Test_pdf.pdf") as pdf_file:
            reader = PdfReader(pdf_file)
            page = len(reader.pages)
        assert page == 3

        folder_zip.close()