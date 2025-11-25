# Desenvolva o seu jogo aqui

# tema: the elder scrolls online

# --- Conteúdo do arquivo 'rpg.py' ---

import sys
import os
import random

# Adiciona o diretório atual ao path para garantir que os módulos sejam encontrados
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importações das classes base
from itens.arma import Arma
from itens.armadura import Armadura
from itens.item import Item
# Importa Heroi com outro nome para evitar conflito com as subclasses
from personagens.heroi import Heroi as HeroiBase 
from personagens.monstro import Monstro

# Importação de TODAS as novas habilidades
from habilidades import ( # <-- CORREÇÃO: "pasta.arquivo"
    ChoqueDestrutivo, EscudoEndurecido, CurarMenor, 
    SoproDeFogo, PeleDeDragao, EstrelaCintilante, CurasRadianas, 
    GolpeDaSombra, MantoDeEvasao, RajadaDeGelo, MatriarcaDeUrso, 
    InvocacaoEsqueleto, ChamaProfana, FluxoArcano, RaioDoDestino
)

# --- Definições de Racas ---
RACAS_ESO = {
    "1": {"nome": "Nord", "vida_bonus": 20, "stamina_bonus": 15, "magicka_bonus": 0, "ataque_bonus": 0, "desc": "Guerreiros robustos, bons com Stamina e Defesa."},
    "2": {"nome": "Dunmer (Elfo Negro)", "magicka_bonus": 20, "ataque_bonus": 5, "vida_bonus": 5, "stamina_bonus": 0, "desc": "Adaptáveis, com afinidade para Magicka e Dano."},
    "3": {"nome": "Altmer (Elfo Alto)", "magicka_bonus": 30, "vida_bonus": 0, "ataque_bonus": 0, "stamina_bonus": 0, "desc": "Nascidos para a Magia, excelente potencial em Magicka."},
    "4": {"nome": "Khajiit", "ataque_bonus": 10, "vida_bonus": 0, "stamina_bonus": 0, "magicka_bonus": 0, "desc": "Povo-Fera ágil, com bônus em dano e furtividade."},
}

# --- Classes de Herói (Subclasses especializadas em Habilidades) ---
class Dragonknight(HeroiBase):
    def __init__(self, nome, raca_info):
        vida_base, ataque_base, defesa_base, magicka_base = 100, 15, 5, 30
        raca_nome = raca_info.get("nome", "Desconhecida")
        super().__init__(nome, vida_base + raca_info.get("vida_bonus", 0), ataque_base + raca_info.get("ataque_bonus", 0), defesa_base, raca_nome) 
        self.classe = "Dragonknight"
        self.magicka_max = magicka_base + raca_info.get("magicka_bonus", 0)
        self.magicka = self.magicka_max
        self.habilidades = [SoproDeFogo(), PeleDeDragao()]

class Templar(HeroiBase):
    def __init__(self, nome, raca_info):
        vida_base, ataque_base, defesa_base, magicka_base = 90, 10, 4, 45
        raca_nome = raca_info.get("nome", "Desconhecida")
        super().__init__(nome, vida_base + raca_info.get("vida_bonus", 0), ataque_base + raca_info.get("ataque_bonus", 0), defesa_base, raca_nome) 
        self.classe = "Templar"
        self.magicka_max = magicka_base + raca_info.get("magicka_bonus", 0)
        self.magicka = self.magicka_max
        self.habilidades = [EstrelaCintilante(), CurasRadianas()]

class Sorcerer(HeroiBase):
    def __init__(self, nome, raca_info):
        vida_base, ataque_base, defesa_base, magicka_base = 80, 12, 3, 50 
        raca_nome = raca_info.get("nome", "Desconhecida")
        super().__init__(nome, vida_base + raca_info.get("vida_bonus", 0), ataque_base + raca_info.get("ataque_bonus", 0), defesa_base, raca_nome) 
        self.classe = "Sorcerer"
        self.magicka_max = magicka_base + raca_info.get("magicka_bonus", 0)
        self.magicka = self.magicka_max
        self.habilidades = [ChoqueDestrutivo(), EscudoEndurecido()]

class Nightblade(HeroiBase):
    def __init__(self, nome, raca_info):
        vida_base, ataque_base, defesa_base, magicka_base = 75, 18, 2, 35
        raca_nome = raca_info.get("nome", "Desconhecida")
        super().__init__(nome, vida_base + raca_info.get("vida_bonus", 0), ataque_base + raca_info.get("ataque_bonus", 0), defesa_base, raca_nome) 
        self.classe = "Nightblade"
        self.magicka_max = magicka_base + raca_info.get("magicka_bonus", 0)
        self.magicka = self.magicka_max
        self.habilidades = [GolpeDaSombra(), MantoDeEvasao()]

class Warden(HeroiBase):
    def __init__(self, nome, raca_info):
        vida_base, ataque_base, defesa_base, magicka_base = 85, 13, 3, 40
        raca_nome = raca_info.get("nome", "Desconhecida")
        super().__init__(nome, vida_base + raca_info.get("vida_bonus", 0), ataque_base + raca_info.get("ataque_bonus", 0), defesa_base, raca_nome) 
        self.classe = "Warden"
        self.magicka_max = magicka_base + raca_info.get("magicka_bonus", 0)
        self.magicka = self.magicka_max
        self.habilidades = [RajadaDeGelo(), MatriarcaDeUrso()]

class Necromancer(HeroiBase):
    def __init__(self, nome, raca_info):
        vida_base, ataque_base, defesa_base, magicka_base = 80, 14, 3, 45
        raca_nome = raca_info.get("nome", "Desconhecida")
        super().__init__(nome, vida_base + raca_info.get("vida_bonus", 0), ataque_base + raca_info.get("ataque_bonus", 0), defesa_base, raca_nome) 
        self.classe = "Necromancer"
        self.magicka_max = magicka_base + raca_info.get("magicka_bonus", 0)
        self.magicka = self.magicka_max
        self.habilidades = [InvocacaoEsqueleto(), ChamaProfana()]

class Arcanist(HeroiBase):
    def __init__(self, nome, raca_info):
        vida_base, ataque_base, defesa_base, magicka_base = 70, 15, 3, 55
        raca_nome = raca_info.get("nome", "Desconhecida")
        super().__init__(nome, vida_base + raca_info.get("vida_bonus", 0), ataque_base + raca_info.get("ataque_bonus", 0), defesa_base, raca_nome) 
        self.classe = "Arcanist"
        self.magicka_max = magicka_base + raca_info.get("magicka_bonus", 0)
        self.magicka = self.magicka_max
        self.habilidades = [FluxoArcano(), RaioDoDestino()]
        self.crux = 0 # Atributo específico do Arcanist

CLASSES_ESO = {
    "1": {"nome": "Dragonknight", "classe_obj": Dragonknight, "desc": "Mestres do Fogo e Tanques robustos."},
    "2": {"nome": "Templar", "classe_obj": Templar, "desc": "Guerreiros da Luz, focados em Cura e Dano Radiante."},
    "3": {"nome": "Sorcerer", "classe_obj": Sorcerer, "desc": "Mestres da Magia, focados em dano elemental e escudos."},
    "4": {"nome": "Nightblade", "classe_obj": Nightblade, "desc": "Assassinos furtivos, especializados em dano de sombra e acertos críticos."},
    "5": {"nome": "Warden", "classe_obj": Warden, "desc": "Protetores da Natureza, usando gelo e invocando animais."},
    "6": {"nome": "Necromancer", "classe_obj": Necromancer, "desc": "Controladores da Morte, usam dano por tempo (DoT) e esqueletos."},
    "7": {"nome": "Arcanist", "classe_obj": Arcanist, "desc": "Invocadores do Arcana, usam o sistema Crux para ataques potentes."},
}

# --- Fim das Definições de Classes ---


# --- Funções do Jogo ---

def menu_principal(heroi):
    print("\n--- MENU PRINCIPAL ---")
    print("1. ℹ️ Status do Herói")
    print("2. 🎒 Inventário")
    print("3. 🌳 Explorar (Iniciar Combate)")
    print("4. 🚪 Sair do Jogo")
    return input("Escolha sua ação (1-4): ").strip()

def criar_heroi():
    print("--- CRIAÇÃO DE PERSONAGEM (The Elder Scrolls Online) ---")
    nome_heroi = input("Qual o nome do seu Herói?: ").strip()
    
    # 1. Escolha de Raça
    print("\n--- Escolha de RAÇA ---")
    for chave, info in RACAS_ESO.items():
        print(f"{chave}. {info['nome']} ({info['desc']})")
        
    while True:
        escolha_raca = input("Escolha sua raça (número): ").strip()
        if escolha_raca in RACAS_ESO:
            raca_info = RACAS_ESO[escolha_raca]
            break
        else:
            print("Escolha de raça inválida.")

    # 2. Escolha de Classe
    print("\n--- Escolha de CLASSE ---")
    for chave, info in CLASSES_ESO.items():
        print(f"{chave}. {info['nome']} - {info['desc']}")
        
    while True:
        escolha_classe = input("Escolha sua classe (número): ").strip()
        if escolha_classe in CLASSES_ESO:
            classe_info = CLASSES_ESO[escolha_classe]
            raca_info = RACAS_ESO[escolha_raca]
            heroi = classe_info['classe_obj'](nome_heroi, raca_info)
            print(f"\n🎉 {heroi.nome}, o {heroi.classe} {raca_info['nome']}, está pronto para a aventura!")
            return heroi
        else:
            print("Escolha de classe inválida.")

def gerar_monstro(heroi):
    # Gera um monstro baseado no nível do herói (simplificação)
    nome, vida, ataque, defesa, xp = "", 0, 0, 0, 0
    if heroi.nivel <= 5:
        nome, vida, ataque, defesa, xp = "Goblin", 30, 8, 2, 50
    elif heroi.nivel <= 10:
        nome, vida, ataque, defesa, xp = "Bandido Orc", 60, 15, 5, 120
    else:
        nome, vida, ataque, defesa, xp = "Troll da Montanha", 100, 20, 8, 250

    return Monstro(nome, vida, ataque, defesa, "Comum", xp, descricao=f"Um perigoso {nome}.")

def menu_combate():
    print("\n--- AÇÃO ---")
    print("1. ⚔️ Ataque Básico")
    print("2. 🛡️ Defender (Aumenta Defesa neste turno)")
    print("3. ✨ Magia/Habilidade")
    print("4. 🏃 Fugir (Chance de falha)")
    return input("Escolha sua ação (1-4): ").strip()

def combate(heroi, monstro):
    print("\n⚔️ --- INÍCIO DA BATALHA --- ⚔️")
    while heroi.esta_vivo() and monstro.esta_vivo():

        # 0. APLICAÇÃO DE DANO POR TEMPO (DOT) NO MONSTRO
        dano_dot = 0
        if monstro.dot_fogo > 0:
            monstro.vida -= monstro.dot_fogo
            dano_dot += monstro.dot_fogo
            # O DoT não se acumula, mas continua o dano a cada turno
            print(f"🔥 Dano por Fogo em {monstro.nome}: {monstro.dot_fogo:.0f}") 
        
        if monstro.dot_profano > 0:
            monstro.vida -= monstro.dot_profano
            dano_dot += monstro.dot_profano
            print(f"🔥 Dano Profano em {monstro.nome}: {monstro.dot_profano:.0f}")

        if dano_dot > 0:
            print(f"DoT: Total de {dano_dot:.0f} de dano aplicado.")
        
        if not monstro.esta_vivo():
            break 
        
        # 1. Turno do Herói
        print(f"\nSeu Turno ({heroi.nome} | HP: {heroi.vida:.0f}/{heroi.vida_max:.0f} | MAG: {heroi.magicka:.0f}/{heroi.magicka_max:.0f})")

        if heroi.classe == "Arcanist":
             print(f" | Crux: {getattr(heroi, 'crux', 0)}/3")

        print(f"Inimigo ({monstro.nome} | HP: {monstro.vida:.0f}/{monstro.vida_max:.0f})")

        # Limpa bônus de defesa temporário
        heroi.defesa_extra_turno = 0

        escolha = menu_combate()

        acao_heroi_concluida = False
        if escolha == '1': # ATAQUE BÁSICO
            heroi.atacar(monstro)
            acao_heroi_concluida = True

        elif escolha == '2': # DEFENDER (Aumento de Defesa para o MONSTRO's turno)
            bonus_defesa = 5 + heroi.defesa // 2 
            heroi.defesa_extra_turno = bonus_defesa 
            print(f"🛡️ {heroi.nome} se prepara, ganhando +{bonus_defesa:.0f} de Defesa neste turno!")
            acao_heroi_concluida = True
            
        elif escolha == '3': # MAGIA/HABILIDADE
            if heroi.habilidades:
                print("\n--- HABILIDADES ---")
                for i, hab in enumerate(heroi.habilidades):
                    print(f"{i+1}. {hab.nome} (Custo: {hab.custo_magicka:.0f} MAG) - {hab.descricao}")
                
                while True:
                    escolha_hab = input("Escolha a habilidade (número) ou 'V' para Voltar: ").strip()
                    if escolha_hab.upper() == 'V':
                        break 
                    try:
                        indice = int(escolha_hab) - 1
                        if 0 <= indice < len(heroi.habilidades):
                            habilidade = heroi.habilidades[indice]
                            if habilidade.usar(heroi, monstro): # Usa a habilidade
                                acao_heroi_concluida = True
                            break
                        else:
                            print("Escolha inválida.")
                    except ValueError:
                        print("Entrada inválida.")
            else:
                print("Você não tem habilidades de classe.")
            
            # Se não usou magia ou voltou, não passa o turno
            if escolha_hab.upper() != 'V' and acao_heroi_concluida == False:
                 continue # Repete o loop do turno do herói

        elif escolha == '4': # FUGIR
            if random.random() < 0.3: # 30% de chance de sucesso
                print("🏃 Você consegue fugir da batalha!")
                return "FUGIU"
            else:
                print("🚨 Falha! O monstro bloqueia sua rota de fuga.")
                acao_heroi_concluida = True
                
        else:
            print("Escolha inválida, você perde seu turno.")
            acao_heroi_concluida = True


        # 2. Turno do Monstro 
        if monstro.esta_vivo() and acao_heroi_concluida:
            # O monstro ataca o herói, considerando a defesa extra do turno
           monstro.atacar(heroi, heroi.defesa_extra_turno)
            
        # O herói recupera uma pequena quantidade de Magicka por turno (Recuperação de Magicka)
        heroi.magicka = min(heroi.magicka_max, heroi.magicka + heroi.magicka_max * 0.05)


    # Fim da Batalha
    if heroi.esta_vivo():
        print(f"\n🏆 {heroi.nome} derrotou o {monstro.nome}!")
        heroi.ganhar_experiencia(monstro.experiencia_recompensa)
        return "VENCEU"
    else:
        print(f"\n💀 {heroi.nome} foi derrotado por {monstro.nome}...")
        return "PERDEU"
        
# --- Loop Principal do Jogo ---
if __name__ == "__main__":
    
    print("Bem-vindo a Tamriel, Herói!")
    heroi = criar_heroi()

    # Itens iniciais (Exemplo)
    heroi.inventario.append(Arma("Cajado de Bordo", "Um cajado simples.", 5))
    heroi.inventario.append(Armadura("Robe de Aprendiz", "Um robe leve.", 2))
    heroi.inventario.append(Item("Poção de Vida", "Restaura 30 de vida."))
    heroi.equipar_item(heroi.inventario[0])
    heroi.equipar_item(heroi.inventario[1])
    
    jogando = True
    while jogando:
        escolha = menu_principal(heroi)
        
        if escolha == '1': 
            print("\n--- STATUS ---")
            print(f"Nome: {heroi.nome} ({heroi.raca} {heroi.classe})")
            print(f"Nível: {heroi.nivel}, XP: {heroi.experiencia:.0f}/{heroi.xp_para_proximo_nivel:.0f}")
            print(f"Vida: {heroi.vida:.0f}/{heroi.vida_max:.0f} | Magicka: {heroi.magicka:.0f}/{heroi.magicka_max:.0f}")
            print(f"Ataque Total: {heroi.ataque:.0f} (Base +{heroi.arma_equipada.bonus_ataque if heroi.arma_equipada else 0})")
            print(f"Defesa Total: {heroi.defesa:.0f} (Base +{heroi.armadura_equipada.bonus_defesa if heroi.armadura_equipada else 0})")
        
        elif escolha == '2':
            print("\n--- INVENTÁRIO (Não Funcional) ---")
            if heroi.inventario:
                for i, item in enumerate(heroi.inventario):
                    equipado = " (Equipado)" if item == heroi.arma_equipada or item == heroi.armadura_equipada else ""
                    print(f"{i+1}. {item.nome} ({item.__class__.__name__}){equipado}")
            else:
                print("Seu inventário está vazio.")

        elif escolha == '3': # EXPLORAR O MUNDO
            if heroi.esta_vivo():
                print("\n🌳 Você caminha pelas planícies de Cyrodiil...")
            
                monstro = gerar_monstro(heroi) 
            
                print(f"Você encontra: {monstro.nome}!")
                print(f"Descrição: {monstro.descricao}")
            
                resultado = combate(heroi, monstro)
                
                if resultado == "PERDEU":
                    print("\nSeu herói foi derrotado. Fim de Jogo!")
                    jogando = False
            else:
                print("\nSeu herói está inconsciente e precisa de um longo descanso.")

        elif escolha == '4': 
            print("Obrigado por jogar! Adeus, e que os Deuses de Tamriel o guiem.")
            jogando = False

        else:
            print("Opção inválida. Tente novamente.")