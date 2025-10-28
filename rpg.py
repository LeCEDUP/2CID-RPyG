# Desenvolva o seu jogo aqui
import time

# ========================
# Classes de Itens e Personagens
# ========================

class Item:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class Arma(Item):
    def __init__(self, nome, descricao, bonus_ataque):
        super().__init__(nome, descricao)
        self.bonus_ataque = bonus_ataque

class Armadura(Item):
    def __init__(self, nome, descricao, bonus_defesa):
        super().__init__(nome, descricao)
        self.bonus_defesa = bonus_defesa

class Heroi:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.inventario = []

def atacar(self, alvo):
        dano = max(0, self.ataque - alvo.defesa)
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano.")
        alvo.receber_dano(dano)

 def receber_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano. Vida atual: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0

    def equipar_item(self, item):
        if hasattr(item, "bonus_ataque"):
            self.ataque += item.bonus_ataque
        if hasattr(item, "bonus_defesa"):
            self.defesa += item.bonus_defesa
        print(f"{self.nome} equipou {item.nome}!")

    def ganhar_experiencia(self, exp):
        print(f"{self.nome} ganhou {exp} de experiência!")

class Monstro:
    def __init__(self, nome, vida, ataque, defesa, tipo):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.tipo = tipo

# ========================
# Função de digitação
# ========================
def narrar(texto, atraso=0.04):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(atraso)
    print()

# ========================
# Introdução temática de Halloween
# ========================
def introducao():
    print("=" * 60)
    print("           🎃 SOMBRAS DE HALLOWEEN: O REINO ROSA EM PERIGO 🎃")
    print("=" * 60)
    time.sleep(1.5)

    narrar("\nÉ véspera de Halloween na cidade encantada de GlitterVille...")
    narrar("As luzes estão fracas, e o ar parece carregado de magia antiga.")
    narrar("As bonecas encantadas tremem — algo desperto se move nas sombras.")
    time.sleep(1.5)

    narrar("\nHá rumores de que Pearl, a criatura dos espelhos quebrados, retornou.")
    narrar("Ela se alimenta da vaidade e transforma reflexos em pesadelos.")
    time.sleep(1.5)

    narrar("\nMas há esperança...")
    narrar("Barbie, a heroína das cores, jura proteger o brilho do mundo humano.")
    narrar("Com sua espada ‘Gloss Hipergrudento’ e o escudo ‘Protetor Térmico’, ela parte em sua missão.")
    narrar("Seu destino? Enfrentar Pearl... e, no fim da jornada, o terrível dragão das trevas: Draculaura.")
    time.sleep(1.5)

    print("\n" + "=" * 60)
    narrar("Pressione ENTER para começar sua aventura assustadora...")
    input()
    print("\n" + "=" * 60)
    time.sleep(1)


