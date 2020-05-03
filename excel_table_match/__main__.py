from pathlib import Path
from excel_table_match.src.reference_file_reader import ReferenceFileReader
from excel_table_match.src.reference_file import ReferenceFile
from excel_table_match.src.target_file_reader import TargetFileReader
from excel_table_match.src.target_file import TargetFile

if __name__ == '__main__':
    filePathRoot = Path.cwd() / 'excel_table_match' / 'files'
    referenceFile: ReferenceFile = ReferenceFileReader(
        filePathRoot / 'example-reference.csv'
    ).read()
    targetFile: TargetFile = TargetFileReader(
        filePathRoot / 'example-target.csv'
    ).read()

    for row in targetFile.targetRows:
        row.get_matches(referenceFile)
        print(row)

    for row in targetFile.targetRows:
        if (row.apolices and row.grupoEconomicos and row.tipos):
            print("Success")
    pass
