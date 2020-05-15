from .header_element import HeaderElement


class ResultHeader:
    def __init__(self):
        self.dateCreated: HeaderElement = HeaderElement(
            0, "DateCreated"
        )
        self.fileName: HeaderElement = HeaderElement(
            1, "FileName"
        )
        self.folderPath: HeaderElement = HeaderElement(
            2, "FileFolder"
        )
        self.apolice: HeaderElement = HeaderElement(
            3, "CONTRATO"
        )
        self.rotina: HeaderElement = HeaderElement(
            4, "ROTINA"
        )
        self.operadora: HeaderElement = HeaderElement(
            5, "OPERADORA"
        )
        self.grupoEconomico: HeaderElement = HeaderElement(
            6, "GRUPO ECONOMICO"
        )
        self.subContrato: HeaderElement = HeaderElement(
            7, "SUBS"
        )
        self.tipo: HeaderElement = HeaderElement(
            8, "TIPO DE ARQUIVO"
        )
        self.error: HeaderElement = HeaderElement(
            9, "Error"
        )
        self.__initialize_header__()

    def write(self, writer):
        writer.writerow(self.header)

    def __initialize_header__(self):
        header = []

        header.insert(self.dateCreated.index, self.dateCreated.content)
        header.insert(self.fileName.index, self.fileName.content)
        header.insert(self.folderPath.index, self.folderPath.content)

        header.insert(self.apolice.index, self.apolice.content)
        header.insert(self.rotina.index, self.rotina.content)
        header.insert(self.operadora.index, self.operadora.content)
        header.insert(self.grupoEconomico.index, self.grupoEconomico.content)
        header.insert(self.subContrato.index, self.subContrato.content)
        header.insert(self.tipo.index, self.tipo.content)

        header.insert(self.error.index, self.error.content)
        self.header = header
