from .base_header import BaseHeader
from .header_element import HeaderElement


class ReferenceHeader(BaseHeader):
    def __init__(self, row):
        super(ReferenceHeader, self).__init__(row)
        self.apolice: ReferenceHeader = self.find_element("CONTRATO")
        self.rotina: ReferenceHeader = self.find_element("ROTINA")
        self.operadora: ReferenceHeader = self.find_element("OPERADORA")
        self.grupoEconomico: ReferenceHeader = self.find_element("GRUPO ECONOMICO")
        self.subContrato: ReferenceHeader = self.find_element("SUBS")
        self.tipo: ReferenceHeader = self.find_element("TIPO DE ARQUIVO")
