from .base_header import BaseHeader
from .header_element import HeaderElement

class TargetHeader(BaseHeader):
    def __init__(self, row):
        super().__init__(row)
        self.date_created: HeaderElement = self.find_element("Date created")
        self.file_name: HeaderElement = self.find_element("File Name")
        self.folder_path: HeaderElement = self.find_element("Folder Path")
