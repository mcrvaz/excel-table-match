class BaseFileReader:
    def __init__(self, fileName):
        self.fileName = fileName

    def get_header(self, reader):
        row = reader.__next__()
        while(self.is_row_empty(row)):
            row = reader.__next__()
        return row

    def is_row_empty(self, row):
        for element in row:
            if element:
                return False
        return True
