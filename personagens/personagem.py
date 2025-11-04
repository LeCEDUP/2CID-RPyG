class Personagem:
    def _init_(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        """Ataque normal: dano = ataque +/- variação - defesa do alvo"""
        variacao = random.randint(-2, 4)  # pequena variação no dano
        dano_bruto = max(0, self.ataque + variacao - alvo.defesa)
        alvo.receber_dano(dano_bruto)
        print(f"{self.nome} atacou {alvo.nome} e causou {dano_bruto} de dano.")

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0

    def esta_vivo(self):
        return self.vida > 0

    def _str_(self):
        return f"{self.nome} (Vida: {self.vida}, Atq: {self.ataque}, Def: {self.defesa})"