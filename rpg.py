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