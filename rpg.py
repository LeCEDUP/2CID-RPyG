import random
import time

INTRODUCAO = """
🌙 Bem-vindo a Vinland — O Despertar do Poço da Corrupção

Há mil anos, o mundo de Vinland florescia em harmonia sob o brilho das três luas.
Reinos prósperos, florestas vivas e magias antigas mantinham o equilíbrio entre luz e sombra.
Mas essa paz terminou quando o feiticeiro Zor’Vek, sedento por poder eterno, abriu o Poço da Corrupção — uma fenda que rasgou o coração do mundo.

Do Poço surgiram criaturas grotescas, moldadas pelo medo, pela morte e pela decadência.
Cidades inteiras foram consumidas, e os deuses silenciaram diante da escuridão crescente.
Somente os Guardiões da Luz, guerreiros escolhidos pela própria essência de Vinland, conseguiram selar o Poço, sacrificando suas almas para conter o mal.

Durante séculos, o mundo permaneceu em paz.
Mas agora, as três luas voltam a se alinhar — e o selo começa a enfraquecer.
O Poço pulsa novamente, espalhando sua influência pelas terras esquecidas.
As antigas bestas despertam de seu sono e a corrupção volta a crescer no coração dos homens.

Você é o último descendente dos Guardiões, herdeiro de um poder ancestral.
Chamado pela profecia e guiado pela luz do destino, deve empunhar uma das armas sagradas —
a Espada do Rei, o Arco Élfico ou o Cajado Arcano — e marchar em direção ao Poço.

Seu dever é selar as trevas mais uma vez.
O futuro de Vinland depende da sua coragem… e da força que habita dentro de você.
"""

def jogar():
    print(INTRODUCAO)

    class Personagem:
        def __init__(self, nome, vida, ataque, defesa):
            self.nome = nome
            self.vida = vida
            self.ataque = ataque
            self.defesa = defesa

        def atacar(self, inimigo):
            dano = self.ataque - inimigo.defesa
            if dano < 0:
                dano = 0
            inimigo.vida -= dano
            print(f"{self.nome} atacou {inimigo.nome} causando {dano} de dano!")

        def esta_vivo(self):
            return self.vida > 0


    class Monstro(Personagem):
        def __init__(self, nome, vida, ataque, defesa, tipo, habilidade):
            super().__init__(nome, vida, ataque, defesa)
            self.tipo = tipo
            self.habilidade = habilidade

        def usar_habilidade(self, inimigo):
            if self.habilidade == "Regeneração":
                cura = random.randint(20, 50)
                self.vida += cura
                print(f"🌿 {self.nome} usa {self.habilidade} e recupera {cura} de vida!")

            elif self.habilidade == "Veneno":
                if random.random() < 0.4:
                    dano = random.randint(15, 30)
                    inimigo.vida -= dano
                    print(f"☠️ {self.nome} envenenou {inimigo.nome}, causando {dano} de dano extra!")

            elif self.habilidade == "Carapaça":
                bonus = random.randint(10, 25)
                self.defesa += bonus
                print(f"🛡️ {self.nome} ativa {self.habilidade}, aumentando defesa em {bonus}!")

            elif self.habilidade == "Ataque Duplo":
                print(f"⚔️ {self.nome} usa {self.habilidade} e ataca duas vezes!")
                self.atacar(inimigo)
                time.sleep(0.5)
                self.atacar(inimigo)

            elif self.habilidade == "Cuspe Ácido":
                dano_extra = random.randint(20, 35)
                inimigo.vida -= dano_extra
                print(f"💧 {self.nome} cospe ácido e causa {dano_extra} de dano verdadeiro!")

            elif self.habilidade == "Evasão":
                if random.random() < 0.3:
                    print(f"💨 {self.nome} esquiva do próximo ataque!")
                    inimigo.ataque -= 30
                    if inimigo.ataque < 0:
                        inimigo.ataque = 0


    class Item:
        def __init__(self, nome, tipo, valor):
            self.nome = nome
            self.tipo = tipo
            self.valor = valor

        def __repr__(self):
            return f"{self.nome}"


    POCAO_CURAR = Item("Poção de Cura", "cura", 100)
    ELIXIR_DANO = Item("Elixir de Dano", "dano", 30)


    monstros = [
        Monstro("Rola-bosta-africano", 420, 65, 50, "BOSTA GIRATÓRIA", "Carapaça"),
        Monstro("Pernilongo", 220, 90, 20, "DENGUE SUPREMA", "Ataque Duplo"),
        Monstro("Mosca-Fedida", 180, 55, 35, "FEDOR MORTAL", "Evasão"),
        Monstro("Verme", 200, 60, 40, "CUSPE ÁCIDO", "Cuspe Ácido"),
        Monstro("Besouro Blindado", 360, 75, 60, "CARAPAÇA DE FERRO", "Carapaça"),
        Monstro("Aranha Venenosa", 250, 95, 25, "VENENO LETAL", "Veneno"),
        Monstro("Louva-a-Deus Mutante", 300, 80, 35, "GOLPE CORTANTE", "Ataque Duplo")
    ]

    def gerar_drop():
        if random.random() < 0.5:
            return random.choice([POCAO_CURAR, ELIXIR_DANO])
        return None


    print("=== 🧙‍♂️ JOGO RPG: BATALHA DE MONSTROS ===\n")
    print("Escolha sua classe:")
    print("1 - Guerreiro (Vida 350, Ataque 55, Defesa 40) — Arma: Espada do Rei (+10 ataque)")
    print("2 - Arqueiro  (Vida 250, Ataque 75, Defesa 20) — Arma: Arco Élfico (+12 ataque)")
    print("3 - Mago      (Vida 200, Ataque 90, Defesa 10) — Arma: Cajado Arcano (+15 ataque)")

    BASES = {
        "Guerreiro": {"vida": 350, "ataque": 55, "defesa": 40, "arma": ("Espada do Rei", 10)},
        "Arqueiro":  {"vida": 250, "ataque": 75, "defesa": 20, "arma": ("Arco Élfico", 12)},
        "Mago":      {"vida": 200, "ataque": 90, "defesa": 10, "arma": ("Cajado Arcano", 15)}
    }

    while True:
        escolha_classe = input("Digite o número da classe: ")
        if escolha_classe == "1":
            classe_nome = "Guerreiro"
            break
        elif escolha_classe == "2":
            classe_nome = "Arqueiro"
            break
        elif escolha_classe == "3":
            classe_nome = "Mago"
            break
        else:
            print("Opção inválida, tente novamente!")

    base = BASES[classe_nome]
    jogador = Personagem(classe_nome, base["vida"], base["ataque"], base["defesa"])
    jogador.arma_nome = base["arma"][0]
    jogador.arma_bonus = base["arma"][1]
    jogador.ataque += jogador.arma_bonus
    jogador.inventario = [POCAO_CURAR, ELIXIR_DANO]
    jogador.habilidade_usada = False
    jogador.base_defesa = base["defesa"]

    print(f"\nVocê escolheu {jogador.nome} — arma equipada: {jogador.arma_nome} (+{jogador.arma_bonus} ataque)")
    print(f"Inventário inicial: {jogador.inventario}\n")

    print("Escolha seu inimigo:")
    for i, m in enumerate(monstros):
        print(f"{i + 1}. {m.nome} ({m.tipo}) — Vida: {m.vida}, Ataque: {m.ataque}, Defesa: {m.defesa}, Habilidade: {m.habilidade}")

    while True:
        escolha_inimigo = input("\nDigite o número do inimigo: ")
        if escolha_inimigo.isdigit() and 1 <= int(escolha_inimigo) <= len(monstros):
            inimigo = monstros[int(escolha_inimigo) - 1]
            break
        print("Opção inválida!")

    print(f"\n⚔️ Você vai enfrentar {inimigo.nome} ({inimigo.tipo})! Prepare-se para a batalha!\n")

    while jogador.esta_vivo() and inimigo.esta_vivo():
        print(f"\n❤️ {jogador.nome}: {jogador.vida} HP | 🧟‍♂️ {inimigo.nome}: {inimigo.vida} HP\n")
        print("Suas ações:")
        print("1 - Atacar")
        print("2 - Defender (aumenta defesa temporariamente)")
        print("3 - Usar item")
        print("4 - Habilidade especial (1x por batalha)")

        acao = input("Escolha sua ação: ")

        if acao == "1":
            jogador.atacar(inimigo)
        elif acao == "2":
            jogador.defesa += 20
            print(f"{jogador.nome} se defende e aumenta sua defesa temporariamente!")
        elif acao == "3":
            if not jogador.inventario:
                print("Você não tem itens!")
            else:
                print("Inventário:", jogador.inventario)
                item_nome = input("Digite o nome do item que quer usar: ")
                item = next((i for i in jogador.inventario if i.nome.lower() == item_nome.lower()), None)
                if item:
                    if item.tipo == "cura":
                        jogador.vida += item.valor
                        print(f"💖 Você usou {item.nome} e recuperou {item.valor} de vida!")
                    elif item.tipo == "dano":
                        jogador.ataque += item.valor
                        print(f"🔥 Você usou {item.nome} e ganhou +{item.valor} de ataque no próximo turno!")
                    jogador.inventario.remove(item)
                else:
                    print("Item não encontrado!")
        elif acao == "4":
            if not jogador.habilidade_usada:
                print(f"💫 {jogador.nome} usa sua habilidade especial!")
                if jogador.nome == "Guerreiro":
                    jogador.defesa += 40
                    print("🛡️ Defesa dobrada por este turno!")
                elif jogador.nome == "Arqueiro":
                    dano_extra = random.randint(50, 80)
                    inimigo.vida -= dano_extra
                    print(f"🏹 Disparo certeiro causa {dano_extra} de dano direto!")
                elif jogador.nome == "Mago":
                    cura = random.randint(60, 100)
                    jogador.vida += cura
                    print(f"✨ Cura mágica restaura {cura} de vida!")
                jogador.habilidade_usada = True
            else:
                print("Você já usou sua habilidade nesta batalha!")
        else:
            print("Ação inválida!")

        if inimigo.esta_vivo():
            time.sleep(1)
            print(f"\n🧟‍♂️ Turno do {inimigo.nome}!")
            inimigo.usar_habilidade(jogador)
            if jogador.esta_vivo():
                inimigo.atacar(jogador)

        jogador.defesa = jogador.base_defesa
        time.sleep(1)

    if jogador.esta_vivo():
        print(f"\n🎉 Você derrotou {inimigo.nome}!")
        drop = gerar_drop()
        if drop:
            jogador.inventario.append(drop)
            print(f"💎 {inimigo.nome} dropou um item: {drop.nome}!")
    else:
        print(f"\n💀 Você foi derrotado por {inimigo.nome}...")
        print("\n========== ☠️ TELA DE MORTE ☠️ ==========")
        print("O eco das trevas consome sua alma...")
        print("1 - Jogar novamente")
        print("2 - Sair do jogo")
        while True:
            escolha = input("O que deseja fazer? ")
            if escolha == "1":
                print("\n🔄 Reiniciando o jogo...\n")
                time.sleep(2)
                jogar()
                break
            elif escolha == "2":
                print("\n👋 Até a próxima, Guardião da Luz...\n")
                exit()
            else:
                print("Opção inválida! Escolha 1 ou 2.")

jogar()
