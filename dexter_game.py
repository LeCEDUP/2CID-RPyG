import random
import time
import sys

# ------------------------------
# Função para pausa com efeito
# ------------------------------
def pausa(texto, delay=1.8):
    """Imprime texto com pausa e flush para funcionar bem no terminal do VS Code"""
    print(texto)
    sys.stdout.flush()
    time.sleep(delay)

# ------------------------------
# CLASSE PRINCIPAL - DEXTER
# ------------------------------
class Dexter:
    def __init__(self):
        self.nome = "Dexter Morgan"
        self.vida = 100
        self.defesa = 10
        self.ataque = 25
        self.passageiro = 30
        self.xp = 0
        self.amostras = []
        self.descoberto = False

    def esta_vivo(self):
        return self.vida > 0
    def atacar(self, alvo):
        dano = max(5, random.randint(self.ataque - 5, self.ataque + 5) - alvo["defesa"])
        pausa(f"🩸 {self.nome} ataca {alvo['nome']} com precisão cirúrgica! Dano: {dano}")
        alvo["vida"] -= dano
        if alvo["vida"] <= 0:
            pausa(f"💀 {alvo['nome']} cai, sem vida.")
            return True
        else:
            # chance de contra-ataque
            if random.random() < 0.4:
                contra = max(3, random.randint(alvo["forca"] - 2, alvo["forca"] + 2) - self.defesa)
                self.vida -= contra
                pausa(f"⚔️ {alvo['nome']} revida! Dexter sofre {contra} de dano!")
            return False

    def sequestrar_e_levar(self, alvo):
        pausa(f"🕶️ {self.nome} segue {alvo['nome']} discretamente pela noite...")
        chance = random.random()
        if chance < 0.7:
            pausa("💉 Emboscada perfeita. O alvo é sedado e levado para a mesa.")
            self.ritual(alvo)
            return True
        else:
            pausa("🚨 O plano falha! O alvo reage e chama a polícia!")
            self.descoberto = True
            return False

    def ritual(self, alvo):
        pausa("🩸 Dexter cobre a sala com plástico... o som do mar ao fundo.")
        time.sleep(2)
        pausa(f"🔪 O ritual é executado. {alvo['nome']} encontra seu destino final.")
        self.xp += 75
        self.passageiro = max(0, self.passageiro - 15)
        self.amostras.append(alvo['nome'])


            def investigar(self, alvo):
        pausa(f"🕵️ {self.nome} investiga {alvo['nome']} nas sombras...")
        time.sleep(2)
        chance = random.random()

        if chance < 0.5:
            pausa(f"🔎 {alvo['nome']} possui um histórico violento... provas encontradas.")
            alvo["culpado"] = True
            alvo["defesa"] += 3
        elif chance < 0.8:
            pausa("❌ Nenhuma prova concreta. O Passageiro começa a sussurrar...")
            self.passageiro = min(100, self.passageiro + 10)
        else:
            pausa(f"🚨 {alvo['nome']} percebe que está sendo seguido!")
            if random.random() < 0.5:
                pausa("😨 Mas Dexter escapa sem ser visto.")
            else:
                pausa("👮 Alguém denuncia Dexter... ele está sob vigilância!")
                self.descoberto = True

    def descansar(self):
        pausa("😴 Dexter retorna ao laboratório para limpar vestígios e refletir.")
        self.vida = min(100, self.vida + 15)
        self.passageiro = max(0, self.passageiro - 5)
        if random.random() < 0.3:
            pausa("📞 Debra liga suspeitando de algo. A tensão aumenta...")
            self.passageiro += 5

    def estado(self):
        print("\n========================")
        print(f"🧠 Estado Mental: {self.estado_mental()}")
        print(f"❤️ Vida: {self.vida}")
        print(f"🩸 Passageiro Sombrio: {self.passageiro}")
        print(f"🔬 Amostras Coletadas: {len(self.amostras)}")
        print(f"🎯 Experiência: {self.xp}")
        print("========================")

    def estado_mental(self):
        if self.passageiro < 40:
            return "Controlado"
        elif self.passageiro < 70:
            return "Instável"
        else:
            return "À beira do colapso"
# ------------------------------
# LISTA DE VILÕES DA SÉRIE
# ------------------------------
viloes = [
    {"nome": "Ice Truck Killer", "vida": 70, "forca": 15, "defesa": 5, "inteligencia": 12, "culpado": True},
    {"nome": "Miguel Prado", "vida": 80, "forca": 18, "defesa": 8, "inteligencia": 15, "culpado": True},
    {"nome": "Doakes", "vida": 100, "forca": 20, "defesa": 10, "inteligencia": 20, "culpado": False},
    {"nome": "Jordan Chase", "vida": 85, "forca": 17, "defesa": 9, "inteligencia": 16, "culpado": True},
    {"nome": "Trinity Killer", "vida": 120, "forca": 25, "defesa": 12, "inteligencia": 22, "culpado": True},
]
# ------------------------------
# EVENTOS EXTRAS
# ------------------------------
def historia_extra(vilao):
    cenas = {
        "Ice Truck Killer": "🚚 Um assassino que desafia Dexter com mensagens de sangue. O jogo psicológico começa.",
        "Miguel Prado": "⚖️ Um promotor e 'amigo' de Dexter... mas a confiança pode ser fatal.",
        "Doakes": "👮 O sargento Doakes desconfia de tudo. Um passo em falso, e tudo acaba.",
        "Jordan Chase": "🎙️ Um guru motivacional que esconde um culto de tortura e morte.",
        "Trinity Killer": "🔔 Um homem comum à primeira vista, mas com um ritual de morte perfeito. O maior desafio de Dexter.",
    }
    pausa(cenas.get(vilao["nome"], "🩸 Um novo perigo surge nas ruas de Miami..."))

def armadilha(dexter, vilao):
    pausa(f"🧠 {dexter.nome} prepara uma armadilha para {vilao['nome']}...")
    chance = random.random()
    if chance < 0.6:
        dano = random.randint(20, 40)
        vilao["vida"] -= dano
        pausa(f"💥 A armadilha explode! {vilao['nome']} sofre {dano} de dano!")
    elif chance < 0.85:
        pausa("😐 A armadilha falha. O vilão escapa ileso.")
    else:
        pausa("🚨 O vilão descobre o plano e denuncia Dexter!")
        dexter.descoberto = True
# ------------------------------
# JOGO PRINCIPAL
# ------------------------------
def jogo():
    dexter = Dexter()
    pausa("⚔️ Dexter Morgan veste suas luvas e afia sua faca cirúrgica.")
    pausa("🌙 Miami dorme... mas o Passageiro Sombrio acorda dentro dele.")

    for vilao in viloes:
        if dexter.descoberto or not dexter.esta_vivo():
            pausa("\n🚔 Dexter foi descoberto... o jogo terminou.")
            break

        pausa(f"\n🎯 NOVO ALVO: {vilao['nome']}")
        pausa(f"📜 Informações: Vida {vilao['vida']} | Defesa {vilao['defesa']} | Inteligência {vilao['inteligencia']}")
        historia_extra(vilao)

        while vilao["vida"] > 0 and dexter.esta_vivo() and not dexter.descoberto:
            print("\nO que Dexter fará?")
            print("1️⃣ Investigar o alvo")
            print("2️⃣ Atacar diretamente")
            print("3️⃣ Sequestrar e levar para a mesa")
            print("4️⃣ Descansar e observar o comportamento")
            print("5️⃣ Criar uma armadilha")
            print("6️⃣ Fugir e mudar de alvo")
            acao = input("Escolha uma opção (1-6): ")

            if acao == "1":
                dexter.investigar(vilao)
            elif acao == "2":
                if dexter.atacar(vilao):
                    pausa("🩸 Um novo troféu foi adicionado à coleção.")
                    break
            elif acao == "3":
                if dexter.sequestrar_e_levar(vilao):
                    break
            elif acao == "4":
                dexter.descansar()
            elif acao == "5":
                armadilha(dexter, vilao)
                if vilao["vida"] <= 0:
                    break
            elif acao == "6":
                if random.random() < 0.4:
                    pausa("💨 Dexter desaparece nas sombras, deixando o alvo para trás.")
                    break
                else:
                    pausa("🚨 Alguém o vê fugindo! Agora está sendo caçado.")
                    dexter.descoberto = True
            else:
                print("❗ Opção inválida.")

            if dexter.passageiro >= 100:
                pausa("\n😈 O Passageiro Sombrio toma o controle. Dexter enlouquece.")
                dexter.descoberto = True
                break

            dexter.estado()

    if dexter.esta_vivo() and not dexter.descoberto:
        pausa("\n🌅 O sol nasce sobre Miami. Mais uma noite termina... por enquanto.")
        dexter.estado()
    else:
        pausa("\n💀 Dexter caiu — pela polícia, por seus demônios, ou pelo destino.")

