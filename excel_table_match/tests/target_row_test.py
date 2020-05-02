import unittest
from pathlib import Path
from typing import List

from excel_table_match.src.target_row import TargetRow
from excel_table_match.src.reference_row import ReferenceRow
from excel_table_match.src.reference_file import ReferenceFile
from excel_table_match.src.reference_file_reader import ReferenceFileReader
from excel_table_match.src.target_file_reader import TargetFileReader
from excel_table_match.src.target_file import TargetFile


def compare_rows(row1, row2, msg=None):
    if len(row1) != len(row2):
        return False
    if len(row1) == 0:
        return True
    for row in row1:
        if not row2.__contains__(row):
            return False
    return True


class TestTargetRowMethods(unittest.TestCase):
    def test_one_exact_match(self):
        filePathRoot: str = Path.cwd() / 'excel_table_match' / 'tests' / 'files'
        referenceFile: ReferenceFile = ReferenceFileReader(
            filePathRoot / 'example-reference.csv'
        ).read()
        targetFile: TargetFile = TargetFileReader(
            filePathRoot / 'example-target.csv'
        ).read()

        targetFile.get_matches(referenceFile)
        expected: List[TargetRow] = [
            TargetRow({'306840'}, {'BRADESCO SPG'}, {'BOLETO'})
        ]
        self.assertTrue(compare_rows(targetFile.targetRows, expected))

    def test_two_exact_matches(self):
        filePathRoot: str = Path.cwd() / 'excel_table_match' / 'tests' / 'files'
        referenceFile: ReferenceFile = ReferenceFileReader(
            filePathRoot / 'example-reference.csv'
        ).read()
        targetFile: TargetFile = TargetFileReader(
            filePathRoot / 'example-target2.csv'
        ).read()

        targetFile.get_matches(referenceFile)
        expected: List[TargetRow] = [
            TargetRow({'306840'}, {'BRADESCO SPG'}, {'BOLETO'}),
            TargetRow({'306841'}, {'BRADESCO SAUDE'}, {'FATURA'})
        ]
        self.assertTrue(compare_rows(targetFile.targetRows, expected))

    def test_one_partial_match(self):
        filePathRoot: str = Path.cwd() / 'excel_table_match' / 'tests' / 'files'
        referenceFile: ReferenceFile = ReferenceFileReader(
            filePathRoot / 'example-reference.csv'
        ).read()
        targetFile: TargetFile = TargetFileReader(
            filePathRoot / 'example-target3.csv'
        ).read()

        targetFile.get_matches(referenceFile)
        expected: List[TargetRow] = [
            TargetRow({'306840'}, {'BRADESCO SPG'}, set())
        ]
        self.assertTrue(compare_rows(targetFile.targetRows, expected))


if __name__ == '__main__':
    unittest.main()
