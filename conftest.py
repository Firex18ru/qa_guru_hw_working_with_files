import pytest
import shutil
import os
from zipfile import ZipFile

files_zip = [
    "tmp/Test_csv.csv",
    "tmp/Test_pdf.pdf",
    "tmp/Test_xlsx.xlsx"
]


@pytest.fixture
def test_zip_folder():
    with ZipFile("folder.zip", "w") as myzip:
        for file in files_zip:
            myzip.write(file)

    os.makedirs("resources", exist_ok=True)
    shutil.move("folder.zip", "resources/folder.zip")
    yield
    shutil.rmtree("resources")
