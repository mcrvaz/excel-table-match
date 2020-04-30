from .HeaderElement import HeaderElement

class BaseHeader:
    def __init__(self, row):
        self.row = row 

    def find_element(self, elementName : str) -> HeaderElement:
        idx = self.row.index(elementName)
        return HeaderElement(idx, elementName)

