import Repository.NotaGsmRepository as respository

def findAll():
    retorno = respository.findAll()
    return retorno

def CadastrarNotaGsm(nota):
    retorno = respository.CadastrarNotaGsm(nota)
    return retorno



def to_dict(self):
    return {
        'tiquete_balanca': self.tiquete_balanca,
        'comissao_motorista': self.comissao_motorista,
        'peso': self.peso,
        'valor_frete': self.valor_frete
    
    }