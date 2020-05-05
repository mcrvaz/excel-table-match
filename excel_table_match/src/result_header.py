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
        self.apolices: HeaderElement = HeaderElement(
            3, "Apolices"
        )
        self.operadoras: HeaderElement = HeaderElement(
            4, "Grupos Economicos"
        )
        self.tipos: HeaderElement = HeaderElement(
            5, "Tipos"
        )
        self.error: HeaderElement = HeaderElement(
            6, "Error"
        )
        self.__initialize_header__()

    def write(self, writer):
        writer.writerow(self.header)

    def __initialize_header__(self):
        header = []
        header.insert(self.dateCreated.index, self.dateCreated.content)
        header.insert(self.fileName.index, self.fileName.content)
        header.insert(self.folderPath.index, self.folderPath.content)
        header.insert(self.apolices.index, self.apolices.content)
        header.insert(self.operadoras.index, self.operadoras.content)
        header.insert(self.tipos.index, self.tipos.content)
        header.insert(self.error.index, self.error.content)
        self.header = header
