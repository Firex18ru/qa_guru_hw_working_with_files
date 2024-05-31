from zipfile import ZipFile
from pypdf import PdfReader
import csv
import zipfile
import openpyxl


def test_pdf(test_zip_folder):
    with ZipFile("resources/folder.zip", "r") as folder_zip:
        with folder_zip.open("Test_pdf.pdf") as pdf_file:
            reader = PdfReader(pdf_file)
            page = len(reader.pages)
        assert page == 3

        folder_zip.close()
