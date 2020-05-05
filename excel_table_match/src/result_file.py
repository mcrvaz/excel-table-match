from typing import List
from .result_header import ResultHeader
from .result_row import ResultRow


class ResultFile:
    def __init__(self, resultHeader: ResultHeader, resultRows: List[ResultRow]):
        self.header = resultHeader
        self.rows = resultRows

    def write(self, writer):
        self.header.write(writer)
        for row in self.rows:
            row.write(writer)
