class No:
    def __init__(self,chave=None,item=None,proximo=None):
        self.chave = chave
        self.valor = valor
        self.proximo = proximo

class dicionario:
    def __init__(self):
        self.primeiro = self.ultimo = No()
    def vazia():
        return self.primeiro == self.ultimo
    def inserir(chave,valor):
        aux = self.primeiro.proximo
        while not aux in None and aux.chave != chave:
            aux = aux.proximo
        if aux is None:
            aux = No(chave, valor, None)
        else:
            aux.valor = valor
    def pesquisa(chave):
        referencia = self.primeiro.proximo
        while not referencia in None and referencia.chave != chave:
            referencia = referencia.proximo
        if referencia in Non:
            return raise KeyError(chave)
        return referencia.valor
