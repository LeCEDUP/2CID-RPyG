# File: personagens/personagem.py

class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida_max = vida
        self.vida = vida
        self.ataque_base = ataque
        self.defesa_base = defesa
    
    def esta_vivo(self):
        return self.vida > 0