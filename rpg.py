import random


EXP_PARA_NIVEL = 20
VIDA_BASE_HEROI = 100
VIDA_POR_NIVEL = 20
ATAQUE_BASE_HEROI = 10
DEFESA_BASE_HEROI = 5
DANO_MAGIA_MIN = 15
DANO_MAGIA_MAX = 25


CONFIG_MONSTROS = {
    "Pequeno": {"vida": 30, "ataque": 5, "defesa": 2, "exp_recompensa": 15, "chance_loot": 0.5},
    "Grande": {"vida": 60, "ataque": 12, "defesa": 5, "exp_recompensa": 30, "chance_loot": 0.7}
}

# -------------------------
# CLASSES BASE
# -------------------------
class Personagem:
    """Classe base para todos os seres vivos no jogo."""
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self._vida_maxima = vida  
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        
        dano = max(1, self.ataque - alvo.defesa) 
        alvo.receber_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")
        if self.vida <= 0:
            print(f"{self.nome} foi derrotado!")

    def esta_vivo(self):
        return self.vida > 0
    
    
    def exibir_status(self):
        print(f"{self.nome} - Vida: {self.vida}/{self._vida_maxima}, Ataque: {self.ataque}, Defesa: {self.defesa}")

# -------------------------
# ITENS (Movidos para cima para clareza da herança)
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

class Pocao(Item):
    def __init__(self, nome, descricao, cura):
        super().__init__(nome, descricao)
        self.cura = cura 

# -------------------------
# HEROI
# -------------------------
class Heroi(Personagem):
    def __init__(self, nome):
        
        super().__init__(nome, vida=VIDA_BASE_HEROI, ataque=ATAQUE_BASE_HEROI, defesa=DEFESA_BASE_HEROI)
        self.nivel = 1
        self.experiencia = 0
        self.inventario = []

    @property
    def vida_maxima_atual(self):
        """Calcula a vida máxima baseada no nível."""
        return VIDA_BASE_HEROI + (self.nivel - 1) * VIDA_POR_NIVEL

    def ganhar_experiencia(self, exp):
        self.experiencia += exp
        print(f"{self.nome} ganhou {exp} de experiência! Total: {self.experiencia}/{EXP_PARA_NIVEL}.")
        while self.experiencia >= EXP_PARA_NIVEL:
            self.experiencia -= EXP_PARA_NIVEL
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self._vida_maxima = self.vida_maxima_atual 
        self.vida = self._vida_maxima 
        self.ataque += 5
        self.defesa += 2
        print(f"**{self.nome} subiu para o nível {self.nivel}!** Status: +20 Vida Máx, +5 Ataque, +2 Defesa.")

    def equipar_item(self, item):
        """Simplificado: Itens são equipados/usados imediatamente e adicionados ao inventário se forem poções."""
        if isinstance(item, Arma):
            
            self.ataque += item.bonus_ataque
            print(f"{self.nome} equipou a arma {item.nome} (+{item.bonus_ataque} ataque)")
        elif isinstance(item, Armadura):
           
            self.defesa += item.bonus_defesa
            print(f"{self.nome} equipou a armadura {item.nome} (+{item.bonus_defesa} defesa)")
        elif isinstance(item, Pocao):
            self.inventario.append(item)
            print(f"{self.nome} adicionou a poção {item.nome} ao inventário!")
        else:
             
             print(f"{self.nome} pegou o item {item.nome}!")

    def lancar_magia(self, alvo):
        dano = random.randint(DANO_MAGIA_MIN, DANO_MAGIA_MAX)
        alvo.receber_dano(dano)
        print(f"{self.nome} lançou magia em {alvo.nome} causando {dano} de dano!")

    def usar_pocao(self):
        
        pocao = next((item for item in self.inventario if isinstance(item, Pocao)), None)
        
        if pocao:
            cura_aplicada = pocao.cura
            self.vida += cura_aplicada
            
            
            if self.vida > self.vida_maxima_atual:
                cura_aplicada -= (self.vida - self.vida_maxima_atual) 
                self.vida = self.vida_maxima_atual
                
            self.inventario.remove(pocao)
            print(f"{self.nome} usou a poção {pocao.nome} e recuperou {cura_aplicada} de vida! ({self.vida}/{self.vida_maxima_atual})")
        else:
            print("Não há poções no inventário!")
            
    def exibir_status(self):
        """Sobrescreve para incluir Nível e XP."""
        super().exibir_status()
        print(f"Nível: {self.nivel} (XP: {self.experiencia}/{EXP_PARA_NIVEL})")
        
        
        poções_no_inv = [item.nome for item in self.inventario if isinstance(item, Pocao)]
        print(f"Inventário (Poções): {', '.join(poções_no_inv) if poções_no_inv else 'Vazio'}")


# -------------------------
# MONSTRO
# -------------------------
class Monstro(Personagem):
    def __init__(self, nome, tipo):
        if tipo not in CONFIG_MONSTROS:
            raise ValueError(f"Tipo de monstro '{tipo}' não reconhecido.")
            
        config = CONFIG_MONSTROS[tipo]
        super().__init__(nome, config["vida"], config["ataque"], config["defesa"])
        self.tipo = tipo
        self.exp_recompensa = config["exp_recompensa"]
        self.chance_loot = config["chance_loot"]

    def loot(self):
        if random.random() < self.chance_loot:
            
            if self.tipo == "Pequeno":
                 
                return random.choice([
                    Pocao("Poção de Cura Básica", "Restaura 20 de vida", 20),
                    Arma("Adaga Envelhecida", "Uma adaga de caça.", 2)
                ])
            else:
                 
                return random.choice([
                    Pocao("Poção de Cura Forte", "Restaura 50 de vida", 50),
                    Armadura("Escudo Leve", "Um escudo simples.", 4)
                ])
        return None

# -------------------------
# MENU DE BATALHA
# -------------------------
def menu_batalha(heroi, monstro):
    print(f"\n\n***Batalha contra {monstro.nome} ({monstro.tipo})!***")
    
    while heroi.esta_vivo() and monstro.esta_vivo():
        print("-" * 30)
        heroi.exibir_status()
        print(f"{monstro.nome} - Vida: {monstro.vida}/{monstro._vida_maxima}")
        print("\n--- Sua vez ---")
        print("1. 🗡️ Atacar")
        print("2. ✨ Lançar magia")
        print("3. 🧪 Usar poção")
        print("4. 📊 Ver Status Detalhado")

        escolha = input("Escolha: ")
        

        acao_feita = False

        if escolha == "1":
            heroi.atacar(monstro)
            acao_feita = True
        elif escolha == "2":
            heroi.lancar_magia(monstro)
            acao_feita = True
        elif escolha == "3":
            
            heroi.usar_pocao()
            acao_feita = True
        elif escolha == "4":
            heroi.exibir_status() 
            continue
        else:
            print("Escolha inválida! Tente novamente.")
            continue
        
        
        if acao_feita and monstro.esta_vivo():
            print("\n--- Turno do Monstro ---")
            monstro.atacar(heroi)
            
    
    print("-" * 30)
    if heroi.esta_vivo():
        print(f"\n🎉 **UUURUU {heroi.nome} derrotou {monstro.nome}!**")
        heroi.ganhar_experiencia(monstro.exp_recompensa) 
        
        loot = monstro.loot()
        if loot:
            print(f"{monstro.nome} dropou {loot.nome}!")
            heroi.equipar_item(loot) 
    else:
        print("\nOOOHH NOOO Você foi derrotado. Fim de jogo.")


# -------------------------
# INÍCIO DO JOGO
# -------------------------
def main():
    print("=" * 30)
    print("=== Bem-vindo ao RPG de Texto Aprimorado ===")
    print("=" * 30)
    nome_heroi = input("Digite o nome do seu herói: ")
    heroi = Heroi(nome_heroi)

    
    espada_inicial = Arma("Espada Curta", "Uma arma de iniciante.", 3)
    armadura_inicial = Armadura("Traje de Couro", "Proteção leve e flexível.", 1)
    pocao_inicial = Pocao("Poção de Iniciante", "Restaura 20 de vida", 20)
    
   
    heroi.equipar_item(espada_inicial)
    heroi.equipar_item(armadura_inicial)
    heroi.equipar_item(pocao_inicial) 
    
    print("\nStatus Inicial do Herói:")
    heroi.exibir_status()

    
    monstros_para_lutar = [
        Monstro("Goblin Patrulheiro", "Pequeno"), 
        Monstro("Orc Brutamontes", "Grande"),
        Monstro("Goblin Guerreiro", "Pequeno"),
        Monstro("Chefão Orc", "Grande")
    ]

    for m in monstros_para_lutar:
        if heroi.esta_vivo():
            menu_batalha(heroi, m)
        else:
            break

    print("\n" + "=" * 30)
    if heroi.esta_vivo():
        print(f"Fim do Jogo! {heroi.nome} sobreviveu a todas as batalhas e chegou ao nível {heroi.nivel}.")
    else:
        print(f"Jogo Encerrado. {heroi.nome} foi derrotado.")
    print("=" * 30)

if __name__ == "__main__":
    main()