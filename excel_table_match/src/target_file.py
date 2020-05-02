from typing import List

from .reference_file import ReferenceFile
from .target_row import TargetRow


class TargetFile:
    def __init__(self, targetRows : List[TargetRow]):
        self.targetRows = targetRows

    def get_matches(self, referenceFile : ReferenceFile):
        for row in self.targetRows:
            row.get_matches(referenceFile)
    
    def write(self):
        return None