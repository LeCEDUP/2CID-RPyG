from personagens.personagem import Personagem
import random

class Monstro(Personagem):
    def __init__(self, nome, vida, ataque, defesa, tipo, recompensa=None, descricao="Um monstro genérico"):
        super().__init__(nome, vida, ataque, defesa)
        self.tipo = tipo
        self.experiencia_recompensa = recompensa if recompensa is not None else random.randint(10, 30)
        self.descricao = descricao
        self.defesa_base = defesa
        self.dot_fogo = 0
        self.dot_profano = 0
        self.congelado = False 
    
    def atacar(self, alvo, bonus_defesa_alvo=0):
        # CHECAGEM DO CONGELAMENTO (CC)
        if self.congelado:
            print(f"🧊 {self.nome} está CONGELADO e perde o turno!")
            self.congelado = False # Limpa o status após perder um turno
            return
        defesa_total_alvo = alvo.defesa + bonus_defesa_alvo
        dano = max(1, self.ataque_base - defesa_total_alvo) 
        alvo.vida -= dano
        print(f"💀 {self.nome} contra-ataca {alvo.nome} causando {dano:.0f} de dano. Vida de {alvo.nome}: {alvo.vida:.0f}")