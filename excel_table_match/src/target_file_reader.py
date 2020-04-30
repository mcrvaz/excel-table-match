import csv
import sys
from typing import List
from .base_file_reader import BaseFileReader
from .target_file import TargetFile
from .target_row import TargetRow
from .target_header import TargetHeader


class TargetFileReader(BaseFileReader):
    def __init__(self, fileName):
        super().__init__(fileName)

    def read(self) -> TargetFile:
        result = list()
        with open(self.fileName, encoding='utf-8-sig') as f:
            reader = csv.reader(f, 'excel', delimiter=';')
            header: TargetHeader = TargetHeader(self.get_header(reader))
            for row in reader:
                if (self.is_row_empty(row)):
                    continue
                result.append(self.create_target_file(row, header))
        return TargetFile(result)

    def create_target_file(self, row, header: TargetHeader) -> TargetRow:
        return TargetRow(
            row[header.date_created.index],
            row[header.file_name.index],
            row[header.folder_path.index],
        )
