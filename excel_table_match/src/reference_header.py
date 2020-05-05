from .base_header import BaseHeader
from .header_element import HeaderElement


class ReferenceHeader(BaseHeader):
    def __init__(self, row):
        super(ReferenceHeader, self).__init__(row)
        self.apolice: ReferenceHeader = super().find_element("CONTRATO")
        self.operadora: ReferenceHeader = super().find_element("OPERADORA")
        self.tipo: ReferenceHeader = super().find_element("TIPO DE ARQUIVO")
