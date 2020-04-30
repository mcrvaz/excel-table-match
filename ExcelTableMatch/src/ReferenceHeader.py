from .BaseHeader import BaseHeader
from .HeaderElement import HeaderElement


class ReferenceHeader(BaseHeader):
    def __init__(self, row):
        super(ReferenceHeader, self).__init__(row)
        self.apolice: ReferenceHeader = super().find_element("Apólice")
        self.grupoEconomico: ReferenceHeader = super().find_element("Grupo Econômico")
        self.tipo: ReferenceHeader = super().find_element("Tipo")
