from typing import Set
from .target_row import TargetRow


class ResultRow:
    def __init__(
        self,
        dateCreated: str,
        fileName: str,
        fileFolder: str,
        contratos: Set[str],
        operadoras: Set[str],
        tipos: Set[str],
        grupoEconomicos: Set[str],
        subContratos: Set[str],
        error: bool
    ):
        self.dateCreated: str = dateCreated
        self.fileName: str = fileName
        self.fileFolder: str = fileFolder

        self.apolices: Set[str] = contratos
        self.operadoras: Set[str] = operadoras
        self.tipos: Set[str] = tipos
        self.grupoEconomicos: Set[str] = grupoEconomicos
        self.subContratos: Set[str] = subContratos

        self.error: bool = error

    @classmethod
    def from_target_row(self, row: TargetRow):
        return self(
            row.dateCreated,
            row.fileName,
            row.fileFolder,
            row.apolices,
            row.operadoras,
            row.tipos,
            row.grupoEconomicos,
            row.subContratos,
            row.error
        )

    def write(self, writer):
        writer.writerow([
            self.dateCreated,
            self.fileName,
            self.fileFolder,
            self.apolices,
            self.operadoras,
            self.tipos,
            self.grupoEconomicos,
            self.subContratos,
            self.error
        ])
