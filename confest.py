import pytest
import shutil
import os
from zipfile import ZipFile

files_zip = ["tmp/Test_csv.csv", "tmp/Test_pdf.pdf", "tmp/Test_xls.xls"]


@pytest.fixture()
def test_zip_folder():
    with ZipFile("folder.zip", "w") as myzip:
        for file in files_zip:
            myzip.write(file)

    # files_zip.write("tmp/Test_csv.csv", arcname="Test_csv.csv", compress_type=zipfile.ZIP_STORED)
    # files_zip.write("tmp/Test_pdf.pdf", arcname="Test_pdf.pdf", compress_type=zipfile.ZIP_STORED)
    # files_zip.write("tmp/Test_xls.xls", arcname="Test_xls.xls", compress_type=zipfile.ZIP_STORED)
    # files_zip.close()

    os.makedirs("resources", exist_ok=True)
    shutil.move("folder.zip", "resources/folder.zip")
    yield
    shutil.rmtree("resources")
