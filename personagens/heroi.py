from personagens.personagem import Personagem

class Heroi(Personagem):
    def __init__(self, nome, vida, ataque, defesa, raca_nome="Aventureiro"): 
        super().__init__(nome, vida, ataque, defesa)
        
        # Atributos de Heroi
        self.nivel = 1
        self.experiencia = 0
        self.xp_para_proximo_nivel = 100
        self.inventario = []
        self.arma_equipada = None
        self.armadura_equipada = None
        
        # ATRIBUTOS NOVOS PARA O SISTEMA ESO
        self.magicka_max = 0 
        self.magicka = 0     
        self.habilidades = [] 
        self.defesa_extra_turno = 0
        self.classe = "Aventureiro"
        self.raca = raca_nome # <--- Armazena o nome da raça aqui
        
    @property
    def ataque(self):
        # Calcula ataque total (Base + Bônus da Arma)
        bonus_arma = self.arma_equipada.bonus_ataque if self.arma_equipada else 0
        return self.ataque_base + bonus_arma
        
    @property
    def defesa(self):
        # Calcula defesa total (Base + Bônus da Armadura)
        bonus_armadura = self.armadura_equipada.bonus_defesa if self.armadura_equipada else 0
        return self.defesa_base + bonus_armadura

    def equipar_item(self, item):
        # Lógica de equipar item (simplificada)
        from itens.arma import Arma
        from itens.armadura import Armadura
        
        if isinstance(item, Arma):
            self.arma_equipada = item
            print(f"✅ {self.nome} equipou {item.nome}.")
        elif isinstance(item, Armadura):
            self.armadura_equipada = item
            print(f"✅ {self.nome} equipou {item.nome}.")
        else:
            print(f"❌ {item.nome} não pode ser equipado.")

    def ganhar_experiencia(self, xp):
        self.experiencia += xp
        print(f"🎉 {self.nome} ganhou {xp} de experiência!")
        while self.experiencia >= self.xp_para_proximo_nivel:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.experiencia -= self.xp_para_proximo_nivel
        self.xp_para_proximo_nivel *= 1.5 
        self.vida_max += 10
        self.vida = self.vida_max 
        self.ataque_base += 2
        self.defesa_base += 1
        self.magicka_max += 5 
        self.magicka = self.magicka_max
        print(f"⬆️ {self.nome} subiu para o Nível {self.nivel}! Atributos aprimorados!")

    def atacar(self, alvo, bonus_defesa=0):
        # O ataque básico do Herói ignora a defesa total do alvo (simplificação)
        dano = max(0, self.ataque - alvo.defesa_base) 
        alvo.vida -= dano
        print(f"💥 {self.nome} ataca {alvo.nome} causando {dano} de dano.")