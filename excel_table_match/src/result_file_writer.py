import csv
from .result_file import ResultFile


class ResultFileWriter:
    def __init__(self, path: str, resultFile: ResultFile):
        self.path = path
        self.file = resultFile

    def write(self):
        with open(self.path, 'w+', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f, dialect='excel', delimiter=';')
            self.file.write(writer)
