from multiprocessing import Manager, Pool, Value
from pathlib import Path

from excel_table_match.src.reference_file import ReferenceFile
from excel_table_match.src.reference_file_reader import ReferenceFileReader
from excel_table_match.src.target_file import TargetFile
from excel_table_match.src.target_file_reader import TargetFileReader
from excel_table_match.src.result_file import ResultFile
from excel_table_match.src.result_file_writer import ResultFileWriter
from excel_table_match.src.result_header import ResultHeader
from excel_table_match.src.result_row import ResultRow


if __name__ == '__main__':
    filePathRoot = Path.cwd() / 'excel_table_match' / 'files'
    referenceFile: ReferenceFile = ReferenceFileReader(
        filePathRoot / 'controle.csv'
    ).read()
    targetFile: TargetFile = TargetFileReader(
        filePathRoot / 'proc.csv'
    ).read()

    count = 0
    percentage = 0
    lastPrint = 0
    interval = 0.01
    rowsCount = len(targetFile.targetRows)
    for row in targetFile.targetRows:
        row.get_matches(referenceFile)
        count += 1
        percentage = count / rowsCount
        if (percentage - lastPrint >= interval):
            lastPrint = percentage
            print(f"{percentage:.0%}")

    resultFile: ResultFile = ResultFile(
        ResultHeader(),
        list(map(ResultRow.from_target_row, targetFile.targetRows))
    )
    ResultFileWriter(
        filePathRoot / 'result.csv',
        resultFile
    ).write()
