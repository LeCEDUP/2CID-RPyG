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

    def atacar(self, alvo):
        dano = max(0, self.ataque - alvo.defesa)
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano.")
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano. Vida atual: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0

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
    print("           🎃 A HALLOWDIVONICAS 🎃")
    print("=" * 60)
    time.sleep(1.5)

    narrar("\nÉ véspera de Halloween na cidade encantada de Glitterkill...")
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

# ========================
# Função de batalha interativa
# ========================
def batalha(hero, inimigo):
    narrar(f"\n--- ⚔️ Batalha contra {inimigo.nome} ---\n")
    while hero.esta_vivo() and inimigo.esta_vivo():
        # Turno do jogador
        print(f"\nSua Vida: {hero.vida} | {inimigo.nome} Vida: {inimigo.vida}")
        print("Escolha sua ação:")
        print("1. Atacar")
        print("2. Usar Poção")
        escolha = input("> ")

        if escolha == "1":
            hero.atacar(inimigo)
        elif escolha == "2":
            pocoes = [item for item in hero.inventario if isinstance(item, Item) and "Poção" in item.nome]
            if pocoes:
                pocao = pocoes[0]
                hero.vida += 30
                hero.inventario.remove(pocao)
                narrar(f"{hero.nome} usou {pocao.nome}. Vida atual: {hero.vida}")
            else:
                narrar("Você não tem poções!")
                continue
        else:
            narrar("Escolha inválida!")
            continue

        # Turno do inimigo
        if inimigo.esta_vivo():
            inimigo.atacar(hero)

    if hero.esta_vivo():
        narrar(f"\n✨ {hero.nome} derrotou {inimigo.nome}! ✨")
        hero.ganhar_experiencia(50)
        return True
    else:
        narrar(f"\n💀 {hero.nome} foi derrotada por {inimigo.nome}... O brilho se apagou.")
        return False

# ========================
# Aventura principal interativa
# ========================
def aventura():
    introducao()

    # Criando personagens
    hero = Heroi("Barbie", 100, 15, 5)
    pearl = Monstro("Pearl", 30, 8, 2, "Pequeno")
    draculaura = Monstro("Draculaura", 200, 30, 10, "Grande")

    # Criando itens
    espada1 = Arma("Gloss Hipergrudento", "Lipsuculento e letal.", 5)
    espeda2 = Arma("Labunizador", "solta labubunês")
    escudo = Armadura("Protetor Térmico", "Um escudo rosa, mas poderoso.", 5)
    pocao_vida = Item("Poção Rosa", "Restaura 30 de vida e um pouco de esperança."1)

    # Inventário inicial
    hero.inventario.append(espada1)
    hero.inventario.append(espada2)
    hero.inventario.append(escudo)
    hero.inventario.append(pocao_vida)
    narrar(f"{hero.nome} encontrou uma {espada.nome}, um {escudo.nome} e uma {pocao_vida.nome}!")

    # Equipar itens
    hero.equipar_item(espada1)
    hero.equipar_item(espada2)
    hero.equipar_item(escudo)
    hero.equipar_item(porcao_vida)



    # Batalha 1
    venceu = batalha(hero, pearl)
    if not venceu:
        return

    # Batalha 2 - desafio final
    venceu = batalha(hero, draculaura)
    if venceu:
        narrar(f"\n🌟 Parabéns, {hero.nome}! Você derrotou {draculaura.nome} e salvou GlitterVille!")
        hero.ganhar_experiencia(200)
    else:
        narrar(f"\n☠️ {hero.nome} foi derrotada pelo {draculaura.nome}... As sombras venceram.")

    print("\n--- 🎃 Fim da Aventura 🎃 ---\n")

# ========================
# Início do jogo
# ========================
if __name__ == "__main__":
    aventura()
