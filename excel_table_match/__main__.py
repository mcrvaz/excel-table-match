from pathlib import Path
from excel_table_match.src.reference_file_reader import ReferenceFileReader
from excel_table_match.src.reference_file import ReferenceFile
from excel_table_match.src.target_file_reader import TargetFileReader
from excel_table_match.src.target_file import TargetFile

if __name__ == '__main__':
    filePathRoot = Path.cwd() / 'excel_table_match' / 'files'
    referenceFileReader: ReferenceFileReader = ReferenceFileReader(
        filePathRoot / 'ANALISE_CARTEIRA.csv'
    )
    referenceFile: ReferenceFile = referenceFileReader.read()

    targetFileReader: TargetFileReader = TargetFileReader(
        filePathRoot / 'Arquivos recebidos PROC.csv'
    )
    targetFile: TargetFile = targetFileReader.read()

    for row in targetFile.targetRows:
        row.get_matches(referenceFile)
        print(row)
    pass
