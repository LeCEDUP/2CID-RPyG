class Heroi(Personagem):
    def _init_(self, nome="Itadori Yuuji", vida=120, ataque=22, defesa=10):
        super()._init_(nome, vida, ataque, defesa)
        self.nivel = 1
        self.experiencia = 0
        self.inventario = []

    def black_flash(self, alvo):
        """
        Golpe crítico especial. Chance baixa (configurável).
        Se falhar, realiza ataque normal.
        """
        chance = 10  # porcentagem de acerto do Black Flash (10%)
        roll = random.randint(1, 100)
        if roll <= chance:
            # dano muito alto
            dano = max(0, int(self.ataque * 4.0) - alvo.defesa)
            alvo.receber_dano(dano)
            print(f"💥 BLACK FLASH! {self.nome} causou {dano} de dano crítico em {alvo.nome}!")
            return True
        else:
            print(f"{self.nome} tentou usar Black Flash... mas falhou.")
            # aplica um ataque normal como penalidade de tentativa
            self.atacar(alvo)
            return False

    def ganhar_experiencia(self, exp):
        self.experiencia += exp
        print(f"{self.nome} ganhou {exp} de experiência. (Total XP: {self.experiencia})")
        # nível sobe a cada 100 XP (padrão)
        while self.experiencia >= 100:
            self.experiencia -= 100
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        aumento_vida = 20
        aumento_ataque = 4
        aumento_defesa = 2
        self.vida += aumento_vida
        self.ataque += aumento_ataque
        self.defesa += aumento_defesa
        print(f"✨ {self.nome} subiu para o nível {self.nivel}! +{aumento_vida} vida, +{aumento_ataque} ataque, +{aumento_defesa} defesa.")

    def equipar_item(self, item):
        # Import interno pra evitar circular imports
        from item import Arma, Armadura
        self.inventario.append(item)
        if isinstance(item, Arma):
            self.ataque += item.bonus_ataque
        elif isinstance(item, Armadura):
            self.defesa += item.bonus_defesa
        print(f"{self.nome} equipou {item.nome}.")
