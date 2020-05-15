from typing import List, Set
from .reference_file import ReferenceFile
from .reference_row import ReferenceRow
from .utils.string_utils import unicode_contains
import time

class TargetRow:
    def __init__(
        self,
        contratos: Set[str],
        operadoras: Set[str],
        tipos: Set[str],
        subContratos: Set[str],
        grupoEconomicos: Set[str],
        dateCreated: str = '',
        fileName: str = '',
        fileFolder: str = ''
    ):
        self.apolices: Set[str] = contratos
        self.operadoras: Set[str] = operadoras
        self.tipos: Set[str] = tipos
        self.subContratos: Set[str] = subContratos
        self.grupoEconomicos: Set[str] = grupoEconomicos

        self.dateCreated: str = dateCreated.strip()
        self.fileName: str = fileName.strip()
        self.fileFolder: str = fileFolder.strip()
        # always penultimate element of the directory
        self.tipo: str = (
            self.fileFolder.split('\\')[-3] if self.fileFolder else ''
        )
        self.fullFileName: str = (
            (self.fileFolder + self.fileName).replace('_', ' ')
        )
        self.error: bool = False
        self.referenceFile: ReferenceFile = None

    @classmethod
    def from_file(self, dateCreated, fileName, fileFolder):
        return self(set(), set(), set(), set(), set(), dateCreated, fileName, fileFolder)

    def get_matches(self, referenceFile: ReferenceFile):
        t1 = time.perf_counter()
        contratoCandidates = self.__get_attribute_matches__(
            referenceFile.apolices
        )
        t2 = time.perf_counter() - t1
        filteredOperadoras = set()
        filteredTipos = set()
        filteredGrupoEconomicos = set()
        filteredSubContratos = set()
        for row in referenceFile.referenceRows:
            if (row.apolice in contratoCandidates):
                filteredOperadoras.add(row.operadora)
                filteredTipos.add(row.tipo)
                filteredGrupoEconomicos.add(row.grupoEconomico)
                filteredSubContratos.add(row.subContrato)
        t3 = time.perf_counter() - t2

        self.apolices = contratoCandidates
        self.operadoras = self.__get_attribute_matches__(filteredOperadoras)
        t4 = time.perf_counter() - t3
        self.tipos = self.__get_attribute_matches__(filteredTipos)
        t5 = time.perf_counter() - t4
        self.grupoEconomicos = self.__get_attribute_matches__(filteredGrupoEconomicos)
        t6 = time.perf_counter() - t5
        self.subContratos = self.__get_attribute_matches__(filteredSubContratos)
        t7 = time.perf_counter() - t6
        self.__filter_matches__(referenceFile)
        t8 = time.perf_counter() - t7
        print(f't1:{t1}, t2:{t2}, t3:{t3}, t4:{t4}, t5:{t5}, t6:{t6}, t7:{t7}, t8:{t8}')

    def __filter_matches__(self, referenceFile: ReferenceFile):
        for ref in referenceFile.referenceRows:
            if self.__is_full_match__(ref):
                self.apolices = {ref.apolice}
                self.operadoras = {ref.operadora}
                self.tipos = {ref.tipo}
                self.subContratos = {ref.subContrato}
                self.grupoEconomicos = {ref.grupoEconomico}
                self.rotina = {ref.rotina}
                return
        self.error = True

    def __is_full_match__(self, row: ReferenceRow):
        return (
            row.apolice in self.apolices and
            row.operadora in self.operadoras and
            row.tipo in self.tipos and
            row.subContrato in self.subContratos and
            row.grupoEconomico in self.grupoEconomicos
        )

    def __get_attribute_matches__(self, attrSet: Set[str]) -> List[str]:
        return { attr for attr in attrSet if attr and unicode_contains(self.fullFileName, attr.strip()) }

    def __eq__(self, row):
        return (
            self.apolices == row.apolices and
            self.operadoras == row.operadoras and
            self.tipos == row.tipos and
            self.grupoEconomicos == row.grupoEconomicos and
            self.subContratos == row.subContratos
        )

    def __ne__(self, row):
        return not (self == row)

    def __str__(self):
        return ("[Contratos: " + str(self.apolices)
                + " Operadoras: " + str(self.operadoras)
                + " Subcontratos: " + str(self.subContratos)
                + " Grupo Economico: " + str(self.grupoEconomicos)
                + " Tipos: " + (str(self.tipos) if self.tipos else f"Tipo encontrado como {self.tipo}") + "]")
