from typing import List
from .target_row import TargetRow

class TargetFile:
    def __init__(self, targetRows : List[TargetRow]):
        self.targetRows = targetRows