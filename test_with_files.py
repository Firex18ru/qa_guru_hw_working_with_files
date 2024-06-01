from zipfile import ZipFile
from pypdf import PdfReader
from io import TextIOWrapper, BytesIO
from openpyxl import load_workbook
import csv


def test_pdf(test_zip_folder):
    with ZipFile("resources/folder.zip", "r") as folder_zip:
        with folder_zip.open("tmp/Test_pdf.pdf") as pdf_file:
            reader = PdfReader(pdf_file)
            page = len(reader.pages)
            assert page == 3

        folder_zip.close()


def test_csv(test_zip_folder):
    with ZipFile("resources/folder.zip", "r") as folder_zip:
        with folder_zip.open("tmp/Test_csv.csv") as csv_file:
            reader = csv.reader(TextIOWrapper(csv_file, encoding="utf-8"))
            return list(reader)
            assert any("1, Dett, male,18,21/05/2015,Great Britain" in row for row in test_csv())


def test_xlsx(test_zip_folder):
    with ZipFile("resources/folder.zip", "r") as folder_zip:
        with folder_zip.open("tmp/Test_xlsx.xlsx") as xlsx_file:
            workbook = load_workbook(BytesIO(xlsx_file.read()))
            sheet = workbook.active
            data = []
            for row in sheet.iter_rows(values_only=True):
                data.append(row)
            return data
            expected_row = "1, Dett, male,18,21/05/2015,Great Britain"
            assert expected_row in test_xls
