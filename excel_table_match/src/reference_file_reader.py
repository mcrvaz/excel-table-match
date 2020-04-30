import csv
import sys
from typing import List
from .base_file_reader import BaseFileReader
from .reference_row import ReferenceRow
from .reference_header import ReferenceHeader
from .reference_file import ReferenceFile


class ReferenceFileReader(BaseFileReader):
    def __init__(self, fileName):
        super().__init__(fileName)

    def read(self) -> ReferenceFile:
        result = list()
        with open(self.fileName, encoding='utf-8-sig') as f:
            reader = csv.reader(f, 'excel', delimiter=';')
            header: ReferenceHeader = ReferenceHeader(self.get_header(reader))
            for row in reader:
                if (self.is_row_empty(row)):
                    continue
                result.append(self.create_reference_file(row, header))
        return ReferenceFile(result)

    def create_reference_file(self, row, header: ReferenceHeader) -> ReferenceRow:
        return ReferenceRow(
            row[header.apolice.index],
            row[header.grupoEconomico.index],
            row[header.tipo.index],
        )
