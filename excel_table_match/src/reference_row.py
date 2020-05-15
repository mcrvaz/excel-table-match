class ReferenceRow:
    def __init__(self, apolice, operadora, tipo, grupoEconomico, subContrato, rotina):
        self.apolice: str = apolice.replace('_', ' ')
        self.operadora: str = operadora.replace('_', ' ')
        self.tipo: str = tipo.replace('_', ' ')
        self.grupoEconomico: str = grupoEconomico.replace('_', ' ')
        self.subContrato: str = subContrato.replace('_', ' ')
        self.rotina: str = rotina.replace('_', ' ')
