import unittest
from excel_table_match.src.target_row import TargetRow


class TargetRowMethods(unittest.TestCase):
    def get_matches(self):
        dateCreated = "22/03/2020"
        fileName = "202003_XPTO_BOLETO_TAIT_COMUNICACOES_306840_0001_BRADESCO_SAUDE.PDF"
        fileFolder = "\\\\xxxxxxxxxx.xxxxx.xxx.xxx\\Integracao\\PROD\\PROC\\BRADESCO\\BOLETO\\202003"
        target = TargetRow(dateCreated, fileName, fileFolder)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
