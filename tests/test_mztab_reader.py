import os
import tempfile
import pandas
from mztab_processing.mztab_reader import read_mztab
 

def test_mztab_reader():
    with tempfile.TemporaryDirectory() as tempdir:
        input_path = os.path.join(os.path.dirname(__file__), "..", "data", "example.mztab")
        read_mztab(input_path, tempdir)
        assert len(os.listdir(tempdir)) == 4

