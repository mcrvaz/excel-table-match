from typing import List, Set
from .reference_file import ReferenceFile
from .utils.string_utils import unicode_contains


class TargetRow:
    def __init__(self, contratos, operadoras, tipos, dateCreated='', fileName='', fileFolder=''):
        self.apolices: Set[str] = contratos
        self.operadoras: Set[str] = operadoras
        self.tipos: Set[str] = tipos
        self.dateCreated: str = dateCreated.strip()
        self.fileName: str = fileName.strip()
        self.fileFolder: str = fileFolder.strip()
        # always penultimate element of the directory
        self.tipo: str = self.fileFolder.split('\\')[-3] if self.fileFolder else ''
        self.fullFileName: str = (
            (self.fileFolder + self.fileName).replace('_', ' ')
        )
        self.error: bool = False
        self.referenceFile = None

    @classmethod
    def from_file(self, dateCreated, fileName, fileFolder):
        return self(set(), set(), set(), dateCreated, fileName, fileFolder)

    def get_matches(self, referenceFile: ReferenceFile = None):
        # if not referenceFile:
        #     referenceFile = self.referenceFile

        contratoCandidates = self.__get_apolice_matches__(
            referenceFile.apolices
        )
        filteredOperadoras = set()
        filteredTipos = set()
        for row in referenceFile.referenceRows:
            if (row.apolice in contratoCandidates):
                filteredOperadoras.add(row.operadora)
                filteredTipos.add(row.tipo)
        self.apolices = contratoCandidates
        self.operadoras = self.__get_operadora_matches__(
            filteredOperadoras
        )
        self.tipos = self.__get_tipo_matches__(filteredTipos)
        self.__filter_matches__(referenceFile)

    def __filter_matches__(self, referenceFile: ReferenceFile):
        for ref in referenceFile.referenceRows:
            if ref.apolice in self.apolices and ref.operadora in self.operadoras and ref.tipo in self.tipos:
                self.apolices = {ref.apolice}
                self.operadoras = {ref.operadora}
                self.tipos = {ref.tipo}
                return
        self.error = True

    def __get_apolice_matches__(self, apoliceList: List[str]) -> List[str]:
        matches: Set[str] = set()
        for apolice in apoliceList:
            _apolice = apolice.strip() if apolice else ''
            if _apolice and _apolice in self.fullFileName:
                matches.add(_apolice)
        return matches

    def __get_operadora_matches__(self, operadoraList: List[str]) -> List[str]:
        matches: Set[str] = set()
        for operadora in operadoraList:
            _operadora = operadora.strip() if operadora else ''
            if _operadora and unicode_contains(self.fullFileName, _operadora):
                matches.add(_operadora)
        return matches

    def __get_tipo_matches__(self, tipoList: List[str]) -> List[str]:
        matches: Set[str] = set()
        for tipo in tipoList:
            _tipo = tipo.strip() if tipo else ''
            if _tipo and unicode_contains(self.tipo, _tipo):
                matches.add(_tipo)
        return matches

    def __eq__(self, row):
        return (self.apolices == row.apolices and
                self.operadoras == row.operadoras and
                self.tipos == row.tipos)

    def __ne__(self, row):
        return not (self == row)

    def __str__(self):
        return ("[Contratos: " + str(self.apolices)
                + " Grupos Econômicos: " + str(self.operadoras)
                + " Tipos: " + (str(self.tipos) if self.tipos else f"Tipo encontrado como {self.tipo}") + "]")
