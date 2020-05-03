from typing import List
from .reference_file import ReferenceFile


class TargetRow:
    def __init__(self, contratos, grupoEconomicos, tipos):
        self.apolices: set = contratos
        self.grupoEconomicos: set = grupoEconomicos
        self.tipos: set = tipos

    @classmethod
    def from_file(self, dateCreated, fileName, fileFolder):
        self.dateCreated: str = dateCreated
        self.fileName: str = fileName
        self.fileFolder: str = fileFolder
        # always penultimate element of the directory
        self.tipo: str = self.fileFolder.split('\\')[-3]
        self.fullFileName: str = (
            (self.fileFolder + self.fileName).replace('_', ' ')
        )
        return self(set(), set(), set())

    def get_matches(self, referenceFile: ReferenceFile):
        contratoCandidates = self.__get_apolice_matches__(
            referenceFile.apolices
        )
        filteredGrupoEconomicos = set()
        filteredTipos = set()
        for row in referenceFile.referenceRows:
            if (row.apolice in contratoCandidates):
                filteredGrupoEconomicos.add(row.grupoEconomico)
                filteredTipos.add(row.tipo)
        grupoEconomicoCandidates = self.__get_grupoEconomico_matches__(
            filteredGrupoEconomicos
        )
        tipoCandidates = self.__get_tipo_matches__(filteredTipos)
        self.apolices = contratoCandidates
        self.grupoEconomicos = grupoEconomicoCandidates
        self.tipos = tipoCandidates
        self.__filter_matches__(referenceFile)

    def __filter_matches__(self, referenceFile: ReferenceFile):
        for ref in referenceFile.referenceRows:
            if ref.apolice in self.apolices and ref.grupoEconomico in self.grupoEconomicos and ref.tipo in self.tipos:
                self.apolices = {ref.apolice}
                self.grupoEconomicos = {ref.grupoEconomico}
                self.tipos = {ref.tipo}
                break

    def __get_apolice_matches__(self, apoliceList: List[str]) -> List[str]:
        matches = set()
        for apolice in apoliceList:
            if apolice in self.fullFileName:
                matches.add(apolice)
        return matches

    def __get_grupoEconomico_matches__(self, grupoEconomicoList: List[str]) -> List[str]:
        matches = set()
        for grupoEconomico in grupoEconomicoList:
            if grupoEconomico and grupoEconomico in self.fullFileName:
                matches.add(grupoEconomico)
        return matches

    def __get_tipo_matches__(self, tipoList: List[str]) -> List[str]:
        matches = set()
        for tipo in tipoList:
            if tipo and tipo in self.tipo:
                matches.add(tipo)
        return matches

    def __eq__(self, row):
        return (self.apolices == row.apolices and
                self.grupoEconomicos == row.grupoEconomicos and
                self.tipos == row.tipos)

    def __ne__(self, row):
        return not (self == row)

    def __str__(self):
        return ("[Contratos: " + str(self.apolices)
                + " Grupos Econômicos: " + str(self.grupoEconomicos)
                + " Tipos: " + (str(self.tipos) if self.tipos else f"Tipo encontrado como {self.tipo}") + "]")
