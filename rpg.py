import random

# -------------------- CLASSES --------------------

class Poder:
    def __init__(self, nome, dano, cooldown_turnos):
        self.nome = nome
        self.dano = dano
        self.cooldown_turnos = cooldown_turnos
        self.turnos_restantes = 0

    def pode_usar(self):
        return self.turnos_restantes == 0

    def usar(self):
        self.turnos_restantes = self.cooldown_turnos

    def passar_turno(self):
        if self.turnos_restantes > 0:
            self.turnos_restantes -= 1

class Heroi:
    def __init__(self, nome, apelido, vida, ataque, defesa, poderes=None):
        self.nome = nome
        self.apelido = apelido
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.poderes = poderes if poderes else []

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, monstro):
        print("\nEscolha um ataque:")
        for i, p in enumerate(self.poderes):
            status = f"(pronto)" if p.pode_usar() else f"(Cooldown: {p.turnos_restantes} turnos)"
            print(f"{i+1} - {p.nome} Dano: {p.dano} {status}")

        try:
            escolha = int(input("Ataque: ")) - 1
        except:
            escolha = -1

        if 0 <= escolha < len(self.poderes):
            poder = self.poderes[escolha]
            if poder.pode_usar():
                dano_total = poder.dano + self.ataque - monstro.defesa
                dano_total = max(dano_total, 0)
                monstro.vida -= dano_total
                print(f"💥 {self.nome} '{self.apelido}' usou {poder.nome} e causou {dano_total} de dano!")
                poder.usar()
            else:
                print(f"⚡ {poder.nome} ainda está em cooldown!")
        else:
            print("Escolha inválida.")

    def passar_turno(self):
        for p in self.poderes:
            p.passar_turno()

class Monstro:
    def __init__(self, nome, vida, ataque, defesa, elemento):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.elemento = elemento

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, heroi):
        dano_total = self.ataque - heroi.defesa
        dano_total = max(dano_total, 0)
        heroi.vida -= dano_total
        print(f"💀 {self.nome} atacou {heroi.nome} '{heroi.apelido}' e causou {dano_total} de dano!")

class Arma:
    def __init__(self, nome, ataque):
        self.nome = nome
        self.ataque = ataque

class Armadura:
    def __init__(self, nome, defesa):
        self.nome = nome
        self.defesa = defesa

class Mochila:
    def __init__(self):
        self.herois = []

    def adicionar(self, heroi):
        self.herois.append(heroi)
        print(f"✨ {heroi.nome} '{heroi.apelido}' foi adicionado à sua mochila!")

    def listar(self):
        if not self.herois:
            print("Sua mochila está vazia.")
        else:
            print("\n👑 Personagens na mochila:")
            for h in self.herois:
                print(f"- {h.nome} '{h.apelido}' | Vida: {h.vida} | Ataque: {h.ataque} | Defesa: {h.defesa}")

# -------------------- FUNÇÕES --------------------

def contar_historia(linhas):
    for linha in linhas:
        print(f"\n{linha}")
        input("Pressione Enter para continuar...")

def batalha(heroi, monstro):
    print(f"\n🔥 Um {monstro.nome} apareceu!")
    while heroi.esta_vivo() and monstro.esta_vivo():
        heroi.atacar(monstro)
        if monstro.esta_vivo():
            monstro.atacar(heroi)
        heroi.passar_turno()
    if heroi.esta_vivo():
        print(f"🎉 {heroi.nome} '{heroi.apelido}' derrotou o {monstro.nome}!")
        return True
    else:
        print(f"💀 {heroi.nome} '{heroi.apelido}' foi derrotado...")
        return False

def abrir_bau(heroi):
    print("\n🎁 Você encontrou um baú!")
    if random.random() < 0.7:
        item = Arma("Espada Flamejante", random.randint(5,15))
        print(f"Você encontrou uma arma: {item.nome} (+{item.ataque} de ataque)")
        heroi.ataque += item.ataque
    else:
        item = Armadura("Armadura de Ferro", random.randint(3,10))
        print(f"Você encontrou uma armadura: {item.nome} (+{item.defesa} de defesa)")
        heroi.defesa += item.defesa

# -------------------- DRAGÕES --------------------

dragao_pyro = Monstro("Dragão Pyro", 120, 25, 10, "Pyro")
dragao_hydro = Monstro("Dragão Hydro", 120, 20, 15, "Hydro")
dragao_anemo = Monstro("Dragão Anemo", 100, 18, 12, "Anemo")
dragao_cryo = Monstro("Dragão Cryo", 110, 22, 14, "Cryo")
dragao_electro = Monstro("Dragão Electro", 115, 23, 13, "Electro")

def batalha_dragao(heroi):
    print("\n🌟 Um Dragão Elemental aparece!")
    dragao = random.choice([dragao_pyro, dragao_hydro, dragao_anemo, dragao_cryo, dragao_electro])
    return batalha(heroi, dragao)

# -------------------- HEROIS DESBLOQUEÁVEIS --------------------

def desbloquear_heroi(mochila):
    suspense = [
        "🌬️ Rumores chegam de um herói poderoso cujo passado é envolto em chamas e mistério...",
        "💫 O vento traz histórias de um combatente lendário que surge para ajudar os viajantes...",
        "✨ Uma luz distante revela a silhueta de um guerreiro extraordinário..."
    ]
    contar_historia([random.choice(suspense)])

    print("\nEscolha o elemento do novo herói:")
    print("1 - Pyro\n2 - Hydro\n3 - Anemo\n4 - Cryo\n5 - Electro")
    escolha = input("Escolha: ")

    if escolha == "1":
        poderes = [Poder("Lança de Fogo", 20,2), Poder("Explosão Flamejante", 30,3), Poder("Inferno Total", 50,5)]
        heroi_novo = Heroi("Diluc", "Sem Apelido", 150, 30, 15, poderes)
    elif escolha == "2":
        poderes = [Poder("Rajada de Água", 18,2), Poder("Tsunami", 28,3), Poder("Maré Devastadora", 48,5)]
        heroi_novo = Heroi("Tartaglia", "Sem Apelido", 140, 28, 18, poderes)
    elif escolha == "3":
        poderes = [Poder("Golpe do Vento", 15,2), Poder("Tornado", 25,3), Poder("Furacão", 40,5)]
        heroi_novo = Heroi("Jean", "Sem Apelido", 130, 25, 20, poderes)
    elif escolha == "4":
        poderes = [Poder("Lança de Gelo", 18,2), Poder("Tempestade Congelante", 27,3), Poder("Nevasca", 45,5)]
        heroi_novo = Heroi("Ganyu", "Sem Apelido", 135, 27, 17, poderes)
    elif escolha == "5":
        poderes = [Poder("Raio", 17,2), Poder("Tempestade Elétrica", 26,3), Poder("Trovão Devastador", 43,5)]
        heroi_novo = Heroi("Fischl", "Sem Apelido", 125, 26, 16, poderes)
    else:
        print("Escolha inválida. Diluc será seu herói por padrão.")
        poderes = [Poder("Lança de Fogo", 20,2), Poder("Explosão Flamejante", 30,3), Poder("Inferno Total", 50,5)]
        heroi_novo = Heroi("Diluc", "Sem Apelido", 150, 30, 15, poderes)

    apelido = input(f"Escolha um apelido para {heroi_novo.nome}: ")
    heroi_novo.apelido = apelido
    mochila.adicionar(heroi_novo)
    print(f"\n🎉 Você desbloqueou {heroi_novo.nome} '{heroi_novo.apelido}'!")

# -------------------- MISSÕES --------------------

class Missao:
    def __init__(self, nome, descricao, monstro):
        self.nome = nome
        self.descricao = descricao
        self.monstro = monstro
        self.concluida = False

    def iniciar(self, heroi):
        print(f"\n🗡️ Missão: {self.nome}")
        print(f"Objetivo: {self.descricao}")
        vitoria = batalha(heroi, self.monstro)
        if vitoria:
            self.concluida = True
            abrir_bau(heroi)
        return vitoria

# Criando missões iniciais
missao1 = Missao("Defender Mondstadt", "Derrote o Hilichurl que ameaça a cidade.", Monstro("Hilichurl", 50, 10, 5, "Pyro"))
missao2 = Missao("Recuperar Poeira Estelar", "Recupere a Poeira Estelar roubada por Slimes Anemo.", Monstro("Slime Anemo", 40, 12, 4, "Anemo"))
missao3 = Missao("Proteger Arconte de Liyue", "Derrote os Fatui que atacam Liyue.", Monstro("Fatui Skirmisher", 60, 15, 8, "Electro"))

missoes = [missao1, missao2, missao3]

# -------------------- LORES --------------------

lore_inicial = [
    "🌌 Você acorda em Teyvat sem memórias e sente o vento misterioso tocar seu rosto...",
    "🗡️ O mundo está cheio de magia, monstros e heróis lendários.",
    "👑 A cidade de Mondstadt precisa de sua ajuda para enfrentar perigos iminentes.",
    "💫 Sua jornada começa agora. Cada batalha revelará mais sobre sua história e sobre Teyvat."
]

# -------------------- MENU --------------------

def menu_principal(heroi, mochila):
    missoes_completadas = 0

    contar_historia(lore_inicial)

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Escolher missão")
        print("2 - Ver status do personagem")
        print("3 - Ver mochila")
        print("4 - Lutar contra Dragão Elemental")
        print("5 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            for i, m in enumerate(missoes):
                status = "✅" if m.concluida else "❌"
                print(f"{i+1} - {m.nome} {status}")
            escolha = input("Escolha a missão: ")
            try:
                idx = int(escolha) - 1
                if 0 <= idx < len(missoes):
                    if not missoes[idx].concluida:
                        vitoria = missoes[idx].iniciar(heroi)
                        if vitoria:
                            missoes_completadas += 1
                            if missoes_completadas % 3 == 0:
                                desbloquear_heroi(mochila)
                                # Criar novas missões aleatórias
                                monstro_novo = Monstro("Abyss Mage", 70, 18, 10, "Cryo")
                                missao_nova = Missao("Explorar Ruínas", "Derrote o Abyss Mage que protege o tesouro.", monstro_novo)
                                missoes.append(missao_nova)
                    else:
                        print("Missão já concluída.")
                else:
                    print("Escolha inválida.")
            except:
                print("Escolha inválida.")

        elif opcao == "2":
            print(f"\n👤 {heroi.nome} '{heroi.apelido}' | Vida: {heroi.vida} | Ataque: {heroi.ataque} | Defesa: {heroi.defesa}")

        elif opcao == "3":
            mochila.listar()

        elif opcao == "4":
            batalha_dragao(heroi)

        elif opcao == "5":
            print("Encerrando jornada...")
            break
        else:
            print("Opção inválida.")

# -------------------- INÍCIO DO JOGO --------------------

def iniciar_jogo():
    mochila = Mochila()
    contar_historia(lore_inicial)

    print("\nEscolha seu gêmeo inicial:")
    print("1 - Lumine")
    print("2 - Aether")
    escolha = input("Escolha: ")
    if escolha == "1":
        gêmeo = "Lumine"
        poderes_iniciais = [Poder("Golpe Leve", 10,1), Poder("Ataque Médio", 20,2), Poder("Ataque Forte", 35,4)]
    else:
        gêmeo = "Aether"
        poderes_iniciais = [Poder("Golpe Leve", 10,1), Poder("Ataque Médio", 20,2), Poder("Ataque Forte", 35,4)]

    apelido = input(f"\nDigite o apelido que você quer dar para {gêmeo}: ")
    heroi = Heroi(gêmeo, apelido, 100, 20, 10, poderes_iniciais)
    print(f"\n✨ Seu personagem é {heroi.nome} '{heroi.apelido}'! Sua jornada começa agora. ✨")
    mochila.adicionar(heroi)
    menu_principal(heroi, mochila)

# -------------------- EXECUÇÃO --------------------

if __name__ == "__main__":
    iniciar_jogo()
