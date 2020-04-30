from typing import List
from ReferenceFile import ReferenceFile


class TargetRow:
    def __init__(self, dateCreated, fileName, fileFolder):
        self.dateCreated = dateCreated
        self.fileName = fileName
        self.fileFolder = fileFolder
        self.fullFileName = self.fileFolder + self.fileName
        self.contratos = None
        self.grupoEconomicos = None
        self.tipos = None

    def get_matches(self, referenceFile: ReferenceFile):
        contratoCandidates = self.get_apolice_matches(referenceFile.apolices)
        filteredGrupoEconomicos = list()
        filteredTipos = list()
        for row in referenceFile.referenceRows:
            if (row.apolice in contratoCandidates):
                filteredGrupoEconomicos.append(row.grupoEconomico)
                filteredTipos.append(row.tipo)
        grupoEconomicoCandidates = self.get_grupoEconomico_matches(
            filteredGrupoEconomicos)
        tipoCandidates = self.get_tipo_matches(filteredTipos)
        self.contratos = contratoCandidates
        self.grupoEconomicos = grupoEconomicoCandidates
        self.tipos = tipoCandidates

    def get_apolice_matches(self, apoliceList: List[str]) -> List[str]:
        matches = list()
        for apolice in apoliceList:
            if apolice in self.fullFileName:
                matches.append(apolice)
        return matches

    def get_grupoEconomico_matches(self, grupoEconomicoList: List[str]) -> List[str]:
        matches = list()
        for grupoEconomico in grupoEconomicoList:
            if grupoEconomico in self.fullFileName:
                matches.append(grupoEconomico)
        return matches

    def get_tipo_matches(self, tipoList: List[str]) -> List[str]:
        matches = list()
        for tipo in tipoList:
            if tipo in self.fullFileName:
                matches.append(tipo)
        return matches

    def __str__(self):
        return ("[Contratos: " + str(self.contratos)
                + " Grupos Econômicos: " + str(self.grupoEconomicos)
                + " Tipos: " + str(self.tipos) + "]")
