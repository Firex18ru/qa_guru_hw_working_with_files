from zipfile import ZipFile
from pypdf import PdfReader
import csv
import zipfile

def test_pdf():
    with zipfile.ZipFile("resources/folder.zip", "r") as zip_folder: