from typing import List
from ReferenceRow import ReferenceRow

class ReferenceFile:
    def __init__(self, referenceRows : List[ReferenceRow]):
        self.referenceRows = referenceRows
        self.apolices = set(map(lambda x: x.apolice, filter(lambda x: x.apolice, referenceRows)))
        self.grupoEconomicos = set(map(lambda x: x.grupoEconomico, filter(lambda x: x.grupoEconomico, referenceRows)))
        self.tipos = set(map(lambda x: x.tipo, filter(lambda x: x.tipo, referenceRows)))