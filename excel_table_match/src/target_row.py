from typing import List
from .reference_file import ReferenceFile


class TargetRow:
    def __init__(self, contratos, grupoEconomicos, tipos):
        self.contratos: set = contratos
        self.grupoEconomicos: set = grupoEconomicos
        self.tipos: set = tipos

    @classmethod
    def from_file(self, dateCreated, fileName, fileFolder):
        self.dateCreated: str = dateCreated
        self.fileName: str = fileName
        self.fileFolder: str = fileFolder
        self.tipo: str = self.fileFolder.split('\\')[-3]
        self.fullFileName: str = (
            self.fileFolder + self.fileName).replace('_', ' ')
        return self(set(), set(), set())

    def get_matches(self, referenceFile: ReferenceFile):
        contratoCandidates = self.get_apolice_matches(referenceFile.apolices)
        filteredGrupoEconomicos = set()
        filteredTipos = set()
        for row in referenceFile.referenceRows:
            if (row.apolice in contratoCandidates):
                filteredGrupoEconomicos.add(row.grupoEconomico)
                filteredTipos.add(row.tipo)
        grupoEconomicoCandidates = self.get_grupoEconomico_matches(
            filteredGrupoEconomicos
        )
        tipoCandidates = self.get_tipo_matches(filteredTipos)
        self.contratos = contratoCandidates
        self.grupoEconomicos = grupoEconomicoCandidates
        self.tipos = tipoCandidates

    def get_apolice_matches(self, apoliceList: List[str]) -> List[str]:
        matches = set()
        for apolice in apoliceList:
            if apolice in self.fullFileName:
                matches.add(apolice)
        return matches

    def get_grupoEconomico_matches(self, grupoEconomicoList: List[str]) -> List[str]:
        matches = set()
        for grupoEconomico in grupoEconomicoList:
            if grupoEconomico and grupoEconomico in self.fullFileName:
                matches.add(grupoEconomico)
        return matches

    def get_tipo_matches(self, tipoList: List[str]) -> List[str]:
        matches = set()
        for tipo in tipoList:
            if tipo and tipo in self.tipo:
                matches.add(tipo)
        return matches

    def __eq__(self, row):
        return (self.contratos == row.contratos and
                self.grupoEconomicos == row.grupoEconomicos and
                self.tipos == row.tipos)

    def __ne__(self, row):
        return not (self == row)

    def __str__(self):
        return ("[Contratos: " + str(self.contratos)
                + " Grupos Econômicos: " + str(self.grupoEconomicos)
                + " Tipos: " + (str(self.tipos) if self.tipos else f"Tipo encontrado como {self.tipo}") + "]")
