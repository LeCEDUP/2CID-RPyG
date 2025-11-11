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

    # -------------------- JOGO --------------------
def jogo():
    sep('=')
    slow("✨ TEYVAT — DESTINOS ENTRELACADOS ✨",0.03)
    sep('=')
    contar_lore(LORE)

    print("Escolha seu gêmeo inicial:")
    print("1 - Aether (♂)\n2 - Lumine (♀)")
    escolha = input("→ ")
    gemeo = "Aether" if escolha=="1" else "Lumine"
    apelido = input("Digite o nome do viajante: ").strip() or "Viajante"

    poderes = [Poder("Ataque Rápido",10,1), Poder("Rajada de Luz",20,2), Poder("Golpe Celestial",35,4)]
    viajante = Heroi(gemeo, "Anemo", apelido, 120, 20, 10, poderes)

    slow(f"\n✨ {apelido} desperta em Teyvat... buscando o reencontro com {'Aether' if gemeo=='Lumine' else 'Lumine'}.",0.03)
    pause()

    moch = Mochila()
    moch.moras = 100
    moch.add_heroi(viajante)
    heroi_ativo = viajante
# -------------------- MISSÕES --------------------
    missoes = [
        ("Floresta do Vento","Um Slime Anemo aparece!", lambda: Monstro("Slime Anemo",60,10,5,"Anemo",30),50),
        ("Caverna Flamejante","Você enfrenta um Pyro Hilichurl!", lambda: Monstro("Hilichurl Pyro",70,14,6,"Pyro",40),70),
        ("Lago das Marés","Um monstro Hydro surge das águas!", lambda: Monstro("Slime Hydro",80,15,7,"Hydro",50),80),
        ("Templo Estático","Relâmpagos cortam o céu!", lambda: Monstro("Hilichurl Electro",90,17,8,"Electro",60),90),
        ("Planalto Congelado","Você pisa em gelo quebradiço...", lambda: Monstro("Slime Cryo",100,18,9,"Cryo",70),100),
        ("Montanha Dourada","Tremores sacodem o solo!", lambda: Monstro("Guardião Geo",110,19,10,"Geo",80),110),
        ("Floresta Selvagem","Raízes emergem do chão!", lambda: Monstro("Slime Dendro",120,20,11,"Dendro",90),120),
        ("Vale das Tempestades","O vento ruge em fúria...", lambda: Monstro("Anemo Elite",130,21,12,"Anemo",100),140),
        ("Portão de Celestia","O ar vibra com poder divino...", lambda: Monstro("Guardião Celestial",150,22,13,"Luz",120),160)
    ]

    while True:
        sep('=')
        print("🌟 MENU PRINCIPAL 🌟")
        print(f"👤 Ativo: {heroi_ativo.status()}")
        print(f"💰 Moras: {moch.moras} | 🍲 Comidas: {len(moch.itens)} | 🧭 Heróis: {len(moch.herois)}")
        sep()
        print("1️⃣ Ver Missões\n2️⃣ Mochila/Heróis\n3️⃣ Cozinhar 🍳\n4️⃣ Trocar Herói 🔄\n5️⃣ Iniciar Missão ⚔️\n6️⃣ Enfrentar Boss 👑\n7️⃣ Sair 🚪")
        sep()
        op = input("Escolha: ")

        if op=="1":
            for i,m in enumerate(missoes,1):
                print(f"{i}. {m[0]} — {m[1]}")
            pause()

        elif op=="2":
            moch.listar_herois()
            moch.listar_itens()
            pause()

        elif op=="3":
            comidas = [{"nome":"Frango Frito 🍗","cura":30,"custo":20},{"nome":"Bolo de Lótus 🍰","cura":60,"custo":50},{"nome":"Teyvat Deluxe 🥘","cura":120,"custo":90}]
            print("🍳 COZINHAR — Escolha um prato:")
            for i,c in enumerate(comidas,1):
                print(f"{i} - {c['nome']} (+{c['cura']}❤️, {c['custo']} moras)")
            esc = input("→ ")
            if esc.isdigit() and 1<=int(esc)<=len(comidas):
                c = comidas[int(esc)-1]
                if moch.moras>=c["custo"]:
                    moch.moras-=c["custo"]
                    moch.add_item(c)
                    print(f"{c['nome']} adicionado à mochila!")
                else:
                    print("💸 Moras insuficientes.")
            else:
                print("Escolha inválida.")
            pause()

        elif op=="4":
            moch.listar_herois()
            esc = input("Trocar para qual herói? ")
            if esc.isdigit() and 1<=int(esc)<=len(moch.herois):
                heroi_ativo = moch.herois[int(esc)-1]
                print(f"{heroi_ativo.apelido} agora é o ativo.")
            pause()

        elif op=="5":
            if not missoes:
                print("Todas as missões concluídas!")
                pause()
                continue
            for i,m in enumerate(missoes,1):
                print(f"{i}. {m[0]}")
            esc = input("→ ")
            if esc.isdigit() and 1<=int(esc)<=len(missoes):
                nome,desc,mf,recompensa = missoes.pop(int(esc)-1)
                sep()
                slow(f"Iniciando {nome}...",0.03)
                slow(desc,0.03)
                sep()
                mon = mf()
                if combate(heroi_ativo,mon,moch):
                    moch.moras+=recompensa
                    print(f"💰 Você ganhou {recompensa} moras!")
                    # Sorteio de novo herói
                    if len(moch.herois)<8:
                        elementos=["Hu Tao","Furina","Raiden","Kaeya","Zhongli","Nahida","Venti"]
                        novo_elem=elementos[len(moch.herois)-1]
                        novo = criar_heroi(novo_elem,novo_elem)
                        moch.add_heroi(novo)
                        print(f"🎉 {novo.nome} se juntou à equipe!")

            pause()

        elif op=="6":
            if missoes:
                print("Conclua todas as 9 missões para liberar Celestia! 👑")
                pause()
                continue
            slow("O céu se rasga. Uma deusa colossal desperta: CELESTIA!",0.03)
            boss = Celestia()
            combate(heroi_ativo,boss,moch)
            if not boss.vivo():
                slow("🌌 Com a queda da deusa, a luz retorna a Teyvat.",0.03)
                slow(f"{apelido} reencontra seu irmão, selando o destino dos dois gêmeos.",0.03)
            pause()

        elif op=="7":
            print("Até a próxima jornada!")
            break

        else:
            print("Opção inválida.")
            pause()

            # -------------------- RODAR --------------------
if __name__=="__main__":
    jogo()


    