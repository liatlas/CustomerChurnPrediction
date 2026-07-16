import pytest
from pathlib import Path

from src.download import verify_dir, verify_csv, download

def test_verify_dir_exists(tmp_path):
    verify_dir(tmp_path)

def test_verify_dir_missing():
    missing = Path("does_not_exist")

    with pytest.raises(FileNotFoundError):
        verify_dir(missing)

def test_verify_csv_exists(tmp_path):
    csv = tmp_path / "test.csv"
    csv.write_text("a,b\n1,2")

    verify_csv("test.csv", tmp_path)

def test_verify_csv_missing(tmp_path):
    with pytest.raises(FileNotFoundError):
        verify_csv("missing.csv", tmp_path)