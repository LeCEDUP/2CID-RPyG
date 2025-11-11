import random, time, sys
# -------------------- EFEITOS DE TEXTO --------------------
def slow(texto, delay=0.03):
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sep(simbolo='-', n=60):
    print(simbolo * n)

def pause():
    input("\n[Pressione Enter para continuar...]\n")
    # -------------------- CLASSES --------------------
class Poder:
    def __init__(self, nome, dano, cooldown):
        self.nome = nome
        self.dano = dano
        self.cooldown = cooldown
        self.cd = 0

    def pronto(self):
        return self.cd == 0

    def usar(self):
        self.cd = self.cooldown

    def tick(self):
        if self.cd > 0:
            self.cd -= 1

class Heroi:
    def __init__(self, nome, elemento, apelido, vida, atk, defe, poderes):
        self.nome = nome
        self.elemento = elemento
        self.apelido = apelido
        self.vida_max = vida
        self.vida = vida
        self.atk = atk
        self.defe = defe
        self.poderes = poderes
        self.exp = 0
        self.nivel = 1

    def vivo(self):
        return self.vida > 0

    def status(self):
        return f"{self.apelido} ({self.elemento}) ❤️ {self.vida}/{self.vida_max} | Nível {self.nivel} | EXP {self.exp}"

    def ganhar_exp(self, qtd):
        self.exp += qtd
        while self.exp >= self.nivel * 50:
            self.exp -= self.nivel * 50
            self.nivel += 1
            self.vida_max += 20
            self.vida = self.vida_max
            self.atk += 5
            self.defe += 3
            print(f"🎉 {self.apelido} subiu para o nível {self.nivel}! Vida, ataque e defesa aumentados!")

    def atacar(self, inimigo):
        print(f"\n⚔️ Turno de {self.apelido}! (EXP do inimigo: {getattr(inimigo,'exp',0)})")
        for i, p in enumerate(self.poderes, 1):
            cd_txt = f"(⏳{p.cd})" if not p.pronto() else ""
            print(f"{i} - {p.nome} {cd_txt}")
        print("0 - Trocar de herói 🔄")
        print("4 - Usar comida 🍲")

        escolha = input("→ ").strip()
        if escolha == "4":
            return "usar_comida"
        if escolha == "0":
            return "trocar_heroi"

        if not escolha.isdigit() or not (1 <= int(escolha) <= len(self.poderes)):
            print("Escolha inválida. Ataque básico realizado.")
            escolha = 1

        poder = self.poderes[int(escolha)-1]
        if not poder.pronto():
            print(f"{poder.nome} ainda está recarregando! Ataque básico.")
            dano = self.atk // 2
        else:
            poder.usar()
            dano = self.atk + poder.dano

        dano_real = max(0, dano - inimigo.defe)
        inimigo.vida -= dano_real
        print(f"{self.apelido} usou {poder.nome} e causou {dano_real} de dano em {inimigo.nome}! 💥")

    def tick_cds(self):
        for p in self.poderes:
            p.tick()

class Monstro:
    def __init__(self, nome, vida, atk, defe, elemento, exp=30):
        self.nome = nome
        self.vida = vida
        self.atk = atk
        self.defe = defe
        self.elemento = elemento
        self.exp = exp

    def vivo(self):
        return self.vida > 0

    def atacar(self, heroi):
        dano = max(1, self.atk - heroi.defe)
        heroi.vida -= dano
        print(f"{self.nome} ataca e causa {dano} de dano em {heroi.apelido}! ⚡ (EXP: {self.exp})")

class Celestia(Monstro):
    def __init__(self):
        super().__init__("Deusa de Celestia 👑", 500, 40, 20, "Luz", 200)
        self.fase = 1

    def atacar_especial(self, herois):
        alvo = random.choice([h for h in herois if h.vivo()])
        dano = random.randint(35, 50)
        alvo.vida -= dano
        print(f"🌩️ {self.nome} lança Luz Divina em {alvo.apelido}, causando {dano} de dano!")

    def troca_fase(self):
        if self.vida < 250 and self.fase == 1:
            self.fase = 2
            print("⚡ Celestia desperta sua forma colossal! Seus ataques dobraram!")
            self.atk *= 2
            # -------------------- MOCHILA --------------------
class Mochila:
    def __init__(self):
        self.moras = 0
        self.itens = []
        self.herois = []

    def add_item(self, item):
        self.itens.append(item)

    def add_heroi(self, h):
        self.herois.append(h)

    def listar_herois(self):
        for i, h in enumerate(self.herois, 1):
            print(f"{i}. {h.status()}")

    def listar_itens(self):
        if not self.itens:
            print("Sem comidas no momento.")
        else:
            for i, item in enumerate(self.itens, 1):
                print(f"{i}. {item['nome']} (+{item['cura']} ❤️)")
                # -------------------- FUNÇÕES AUXILIARES --------------------
def usar_comida_em_heroi(moch, h):
    moch.listar_itens()
    esc = input("Escolha comida: ")
    if esc.isdigit() and 1 <= int(esc) <= len(moch.itens):
        c = moch.itens.pop(int(esc)-1)
        h.vida = min(h.vida_max, h.vida + c["cura"])
        print(f"{h.apelido} comeu {c['nome']} e recuperou {c['cura']} de vida! ❤️")
    else:
        print("Inválido.")

def criar_heroi(personagem, apelido=None):
    ataques = {
        "Hu Tao": ["Explosão Flamejante", "Lança Ígnea", "Inferno Carmesim"],
        "Furina": ["Onda Purificadora", "Chuva Sagrada", "Mar Revolto"],
        "Raiden": ["Descarga Rápida", "Relâmpago Cortante", "Tormenta Púrpura"],
        "Kaeya": ["Lâmina Gélida", "Sopro Ártico", "Nevasca Glacial"],
        "Zhongli": ["Golpe Rochoso", "Terra Colapsante", "Montanha Dourada"],
        "Nahida": ["Crescimento Selvagem", "Esporos Venenosos", "Raízes Ancestrais"],
        "Venti": ["Corte de Vento", "Rajada Espiral", "Fúria Tempestuosa"]
    }
    nomes = ataques[personagem]
    poderes = [Poder(nomes[0], 10, 1), Poder(nomes[1], 20, 2), Poder(nomes[2], 35, 4)]
    apelido = apelido or personagem
    return Heroi(personagem, personagem, apelido, 120, 20, 10, poderes)

def combate(heroi, inimigo, moch):
    sep()
    slow(f"⚔️ Batalha contra {inimigo.nome}! EXP do inimigo: {getattr(inimigo,'exp',0)}", 0.03)
    sep()
    while any(h.vivo() for h in moch.herois) and inimigo.vivo():
        acao = heroi.atacar(inimigo)
        if acao == "usar_comida":
            usar_comida_em_heroi(moch, heroi)
            continue
        if acao == "trocar_heroi":
            moch.listar_herois()
            esc = input("Escolha herói para trocar: ")
            if esc.isdigit() and 1 <= int(esc) <= len(moch.herois):
                heroi = moch.herois[int(esc)-1]
                print(f"{heroi.apelido} agora é o ativo!")
            continue

        if isinstance(inimigo, Celestia):
            inimigo.troca_fase()
            if random.random() < 0.3:
                inimigo.atacar_especial([heroi])

        if inimigo.vivo():
            inimigo.atacar(heroi)

        for h in moch.herois:
            h.tick_cds()
        sep()

    if any(h.vivo() for h in moch.herois):
        slow(f"🏆 Vitória! {inimigo.nome} derrotado!", 0.03)
        for h in moch.herois:
            if h.vivo():
                h.ganhar_exp(getattr(inimigo,'exp',30))
                 # Baú aleatório
        if random.random() < 0.7:
            baus = [{"nome":"Frango Frito 🍗","cura":30},{"nome":"Bolo de Lótus 🍰","cura":60},{"nome":"Teyvat Deluxe 🥘","cura":120}]
            c = random.choice(baus)
            moch.add_item(c)
            print(f"🗝️ Você encontrou um baú e obteve {c['nome']}! (+{c['cura']}❤️)")
        return True
    else:
        slow(f"💀 Todos os heróis foram derrotados...", 0.03)
        return False
    # -------------------- HISTÓRIA --------------------
LORE = """
Em um universo onde inúmeros mundos florescem e morrem,
dois gêmeos viajavam através das estrelas.

Eles não pertenciam a nenhum reino,
mas todos os reinos pertenciam às suas memórias.

Certo dia, ao tentar atravessar um mundo corrompido pela guerra e pela magia,
uma deusa desconhecida surgiu diante deles.

Com um gesto, ela separou os dois irmãos,
selando um e lançando o outro nas profundezas do tempo e do espaço...
"""

def contar_lore(lore):
    sep("=")
    slow(lore, 0.03)
    sep("=")
    pause()
    

    