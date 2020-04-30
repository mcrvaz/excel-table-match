from ReferenceFileReader import ReferenceFileReader
from TargetFileReader import TargetFileReader
from ReferenceFileReader import ReferenceFileReader
from TargetFile import TargetFile
from ReferenceFile import ReferenceFile
from TargetRow import TargetRow

if __name__ == '__main__':
    referenceFileReader : ReferenceFileReader = ReferenceFileReader('files/ANALISE_CARTEIRA.csv')
    referenceFile : ReferenceFile = referenceFileReader.read()

    targetFileReader : TargetFileReader = TargetFileReader('files/Arquivos recebidos PROC.csv')
    targetFile : TargetFile = targetFileReader.read()
    
    for row in targetFile.targetRows:
        row.get_matches(referenceFile)
        print(row)
    pass