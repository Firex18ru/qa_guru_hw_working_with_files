import zipfile

import pytest
import shutil
import os

files_zip = ["tmp/Test_csv.csv", "tmp/Test_pdf.pdf", "tmp/Test_xls.xls"]


@pytest.fixture(scope='function', autouse=True)
def test_zip_folder():
    files_zip = zipfile.ZipFile("tmp/folder.zip", "w")
    files_zip.write("tmp/Test_csv.csv", arcname="Test_csv.csv", compress_type=zipfile.ZIP_STORED)
    files_zip.write("tmp/Test_pdf.pdf", arcname="Test_pdf.pdf", compress_type=zipfile.ZIP_STORED)
    files_zip.write("tmp/Test_xls.xls", arcname="Test_xls.xls", compress_type=zipfile.ZIP_STORED)
    files_zip.close()

    new_folder = "resources"
    os.makedirs(new_folder, exist_ok=True)
    yield
    shutil.rmtree("resources")
