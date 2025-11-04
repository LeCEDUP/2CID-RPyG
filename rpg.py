#rpg
class Item:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def __str__(self):
        return f"{self.nome}: {self.descricao}"
    
    class Arma(Item):
        def __init__(self, nome, descricao, dano):
            super().__init__(nome, descricao)
            self.dano = dano