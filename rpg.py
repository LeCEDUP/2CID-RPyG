import random

# -------------------------
# CLASSES BASE
# -------------------------
class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa  

    def atacar(self, alvo):
        dano = self.ataque - alvo.defesa
        dano = max(dano, 0)  
        alvo.receber_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")

    def esta_vivo(self):
        return self.vida > 0


# -------------------------
# HEROI
# -------------------------
class Heroi(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=100, ataque=10, defesa=5)
        self.nivel = 1
        self.experiencia = 0
        self.inventario = []

    def ganhar_experiencia(self, exp):
        self.experiencia += exp
        print(f"{self.nome} ganhou {exp} de experiência!")
        while self.experiencia >= 20:
            self.experiencia -= 20
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.vida += 20
        self.ataque += 5
        self.defesa += 2
        print(f"{self.nome} subiu para o nível {self.nivel}!")

    def equipar_item(self, item):
        if isinstance(item, Arma):
            self.ataque += item.bonus_ataque
            print(f"{self.nome} equipou a arma {item.nome} (+{item.bonus_ataque} ataque)")
        elif isinstance(item, Armadura):
            self.defesa += item.bonus_defesa
            print(f"{self.nome} equipou a armadura {item.nome} (+{item.bonus_defesa} defesa)")

    def lancar_magia(self, alvo):
        dano = random.randint(15, 25)
        alvo.receber_dano(dano)
        print(f"{self.nome} lançou magia em {alvo.nome} causando {dano} de dano!")


# -------------------------
# MONSTRO
# -------------------------
class Monstro(Personagem):
    def __init__(self, nome, tipo):
        if tipo == "Pequeno":
            vida = 30
            ataque = 5
            defesa = 2
        else:
            vida = 60
            ataque = 12
            defesa = 5
        super().__init__(nome, vida, ataque, defesa)
        self.tipo = tipo


# -------------------------
# ITENS
# -------------------------
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


# -------------------------
# JOGO SIMPLES
# -------------------------
def menu_batalha(heroi, monstro):
    while heroi.esta_vivo() and monstro.esta_vivo():
        print("\n--- Sua vez ---")
        print("1. Atacar")
        print("2. Lançar magia")
        print("3. Ver status")
        escolha = input("Escolha: ")

        if escolha == "1":
            heroi.atacar(monstro)
        elif escolha == "2":
            heroi.lancar_magia(monstro)
        elif escolha == "3":
            print(f"{heroi.nome} - Vida: {heroi.vida}, Ataque: {heroi.ataque}, Defesa: {heroi.defesa}")
            continue
        else:
            print("Escolha inválida!")
            continue

        if monstro.esta_vivo():
            monstro.atacar(heroi)

    if heroi.esta_vivo():
        print(f"\nParabéns! {heroi.nome} derrotou {monstro.nome}!")
        heroi.ganhar_experiencia(15)
    else:
        print("\nVocê foi derrotado. Fim de jogo.")


# -------------------------
# INÍCIO DO JOGO
# -------------------------
def main():
    print("=== Bem-vindo ao RPG de Texto ===")
    nome_heroi = input("Digite o nome do seu herói: ")
    heroi = Heroi(nome_heroi)

    # ADD ITENS INICIAIS
    espada = Arma("Espada de Ferro", "Uma espada básica.", 5)
    armadura = Armadura("Couraça Simples", "Proteção básica.", 3)
    heroi.inventario.extend([espada, armadura])
    heroi.equipar_item(espada)
    heroi.equipar_item(armadura)

    # CRIANDO MONSTRO
    goblin = Monstro("Goblin", "Pequeno")

    # MENU DE BATALHA
    menu_batalha(heroi, goblin)


if __name__ == "__main__":
    main()
