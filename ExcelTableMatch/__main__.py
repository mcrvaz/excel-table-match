from pathlib import Path
from ExcelTableMatch.src.ReferenceFileReader import ReferenceFileReader
from ExcelTableMatch.src.ReferenceFile import ReferenceFile
from ExcelTableMatch.src.TargetFileReader import TargetFileReader
from ExcelTableMatch.src.TargetFile import TargetFile

if __name__ == '__main__':
    filePathRoot = Path.cwd() / 'ExcelTableMatch' / 'files'
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
