class NotaGsm:
    def __init__(self, id_nota, tiquete_balanca, comissao_motorista, peso, valor_frete):
        self.id_nota = id_nota
        self.tiquete_balanca = tiquete_balanca
        self.comissao_motorista = comissao_motorista
        self.peso = peso
        self.valor_frete = valor_frete

    def to_dict(self):
        return {
             'id_nota': self.id_nota,
            'tiquete_balanca': self.tiquete_balanca,
            'comissao_motorista': self.comissao_motorista,
            'peso': self.peso,
            'valor_frete': self.valor_frete
        }