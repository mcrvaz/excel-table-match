from typing import List
from .reference_row import ReferenceRow

class ReferenceFile:
    def __init__(self, referenceRows : List[ReferenceRow]):
        self.referenceRows = referenceRows
        self.apolices = set(map(lambda x: x.apolice, filter(lambda x: x.apolice, referenceRows)))
        self.operadoras = set(map(lambda x: x.operadora, filter(lambda x: x.operadora, referenceRows)))
        self.tipos = set(map(lambda x: x.tipo, filter(lambda x: x.tipo, referenceRows)))
        self.subContratos = set(map(lambda x: x.subContrato, filter(lambda x: x.subContrato, referenceRows)))
        self.rotinas = set(map(lambda x: x.rotina, filter(lambda x: x.rotina, referenceRows)))
