from typing import List
from .reference_row import ReferenceRow

class ReferenceFile:
    def __init__(self, referenceRows : List[ReferenceRow]):
        self.referenceRows = referenceRows
        self.apolices = list(map(lambda x: x.apolice, filter(lambda x: x.apolice, referenceRows)))
        self.operadoras = list(map(lambda x: x.operadora, filter(lambda x: x.operadora, referenceRows)))
        self.tipos = list(map(lambda x: x.tipo, filter(lambda x: x.tipo, referenceRows)))