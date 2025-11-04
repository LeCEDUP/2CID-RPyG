# --- Conteúdo do arquivo 'habilidades.py' ---

import random

class Habilidade:
    """Classe base para todas as habilidades de classe."""
    def __init__(self, nome, custo_magicka, descricao):
        self.nome = nome
        self.custo_magicka = custo_magicka
        self.descricao = descricao

    def usar(self, atacante, alvo=None):
        """Método a ser sobrescrito. Retorna True se o custo for pago."""
        if atacante.magicka < self.custo_magicka:
            print("Magicka insuficiente!")
            return False
        
        atacante.magicka -= self.custo_magicka
        return True 

# ----------------- HABILIDADES DAS CLASSES -----------------

# SORCERER (Magia de Choque, Escudos)
class ChoqueDestrutivo(Habilidade):
    def __init__(self):
        super().__init__("Choque Destrutivo", 15, "Lança relâmpago que causa dano mágico.")
    def usar(self, atacante, alvo):
        if super().usar(atacante, alvo):
            dano_magico = atacante.ataque + 10 
            alvo.vida -= dano_magico
            print(f"⚡ {atacante.nome} canaliza um relâmpago em {alvo.nome}, causando {dano_magico:.0f} de dano MÁGICO!")
            return True
        return False

class EscudoEndurecido(Habilidade):
    def __init__(self):
        super().__init__("Escudo Endurecido", 10, "Ganha grande bônus de Defesa neste turno.")
    def usar(self, atacante, alvo=None): 
        if super().usar(atacante, atacante): 
            bonus_defesa = 5 + atacante.nivel * 3
            atacante.defesa_extra_turno = bonus_defesa
            print(f"🛡️ {atacante.nome} conjura um Escudo Endurecido, ganhando +{bonus_defesa:.0f} de Defesa neste turno!")
            return True
        return False

# CLASSE NECESSÁRIA PARA CORRIGIR O IMPORT
class CurarMenor(Habilidade):
    def __init__(self):
        super().__init__("Curar Menor", 12, "Cura uma pequena quantidade de vida.")
    def usar(self, atacante, alvo=None): 
        if super().usar(atacante, atacante):
            cura = 20 + atacante.nivel * 2
            atacante.vida = min(atacante.vida_max, atacante.vida + cura)
            print(f"✨ {atacante.nome} se cura em {cura:.0f} de vida. Vida atual: {atacante.vida}/{atacante.vida_max}")
            return True
        return False
        
# DRAGONKNIGHT (Fogo, Tanque)
class SoproDeFogo(Habilidade):
    def __init__(self):
        super().__init__("Sopro de Fogo", 15, "Causa dano de fogo e um pequeno DoT (Dano por Turno).")
    def usar(self, atacante, alvo):
        if super().usar(atacante, alvo):
            dano = atacante.ataque * 0.8 + 5
            alvo.vida -= dano
            alvo.dot_fogo = 5 
            print(f"🔥 {atacante.nome} usa Sopro de Fogo, causando {dano:.0f} de dano e acendendo um DoT!")
            return True
        return False

class PeleDeDragao(Habilidade):
    def __init__(self):
        super().__init__("Pele de Dragão", 10, "Aumenta permanentemente a Defesa e se cura levemente.")
    def usar(self, atacante, alvo=None):
        if super().usar(atacante, atacante):
            bonus_defesa = 1
            cura = 10
            atacante.defesa_base += bonus_defesa
            atacante.vida = min(atacante.vida_max, atacante.vida + cura)
            print(f"⛰️ {atacante.nome} endurece sua pele, aumentando Defesa em {bonus_defesa} e se curando em {cura}.")
            return True
        return False

# TEMPLAR (Luz, Cura)
class EstrelaCintilante(Habilidade):
    def __init__(self):
        super().__init__("Estrela Cintilante", 18, "Dano massivo de luz no alvo, ignorando defesa.")
    def usar(self, atacante, alvo):
        if super().usar(atacante, alvo):
            dano = atacante.ataque + 15
            alvo.vida -= dano
            print(f"☀️ {atacante.nome} invoca uma Estrela Cintilante, causando {dano:.0f} de dano MASSIVO de luz!")
            return True
        return False

class CurasRadianas(Habilidade):
    def __init__(self):
        super().__init__("Curas Radianas", 15, "Cura moderada para si mesmo e restaura Magicka.")
    def usar(self, atacante, alvo=None):
        if super().usar(atacante, atacante):
            cura = 30 + atacante.nivel * 3
            magicka_restaurada = 5
            atacante.vida = min(atacante.vida_max, atacante.vida + cura)
            atacante.magicka = min(atacante.magicka_max, atacante.magicka + magicka_restaurada)
            print(f"✨ {atacante.nome} é banhado em luz, curando {cura:.0f} de vida e restaurando {magicka_restaurada} MAG.")
            return True
        return False

# NIGHTBLADE (Sombra, DPS)
class GolpeDaSombra(Habilidade):
    def __init__(self):
        super().__init__("Golpe da Sombra", 15, "Ataque furtivo com alta chance de Acerto Crítico (2x Dano).")
    def usar(self, atacante, alvo):
        if super().usar(atacante, alvo):
            dano = atacante.ataque
            if random.random() < 0.4: # 40% de chance de crítico
                dano *= 2
                print("🔪 ACERTO CRÍTICO!")
            alvo.vida -= dano
            print(f"🌑 {atacante.nome} ataca das sombras, causando {dano:.0f} de dano.")
            return True
        return False

class MantoDeEvasao(Habilidade):
    def __init__(self):
        super().__init__("Manto de Evasão", 10, "Ganha um bônus de Defesa massivo temporário.")
    def usar(self, atacante, alvo=None):
        if super().usar(atacante, atacante):
            bonus_defesa = 10 + atacante.nivel * 2
            atacante.defesa_extra_turno = bonus_defesa
            print(f"🌫️ {atacante.nome} se esvai nas sombras, ganhando +{bonus_defesa:.0f} de Defesa neste turno!")
            return True
        return False
        
# WARDEN (Natureza, Gelo, Invocação)
class RajadaDeGelo(Habilidade):
    def __init__(self):
        super().__init__("Rajada de Gelo", 15, "Dano de gelo com chance de CONGELAR o alvo (perder o próximo turno).")
    def usar(self, atacante, alvo):
        if super().usar(atacante, alvo):
            dano = atacante.ataque * 0.9
            alvo.vida -= dano
            if random.random() < 0.25: # 25% de chance de congelar
                alvo.congelado = True 
                print("❄️ O alvo foi CONGELADO e perderá o próximo turno!")
            print(f"🧊 {atacante.nome} atira gelo, causando {dano:.0f} de dano.")
            return True
        return False

class MatriarcaDeUrso(Habilidade):
    def __init__(self, dano_base=10):
        super().__init__("Matriarca de Urso", 20, "Invoca um urso que ataca imediatamente.")
        self.dano_base = dano_base
    def usar(self, atacante, alvo):
        if super().usar(atacante, alvo):
            dano = self.dano_base + atacante.nivel * 2
            alvo.vida -= dano
            print(f"🐻 {atacante.nome} invoca um Urso. O urso ataca o alvo, causando {dano:.0f} de dano.")
            return True
        return False

# NECROMANCER (Morte, Dano por Tempo)
class InvocacaoEsqueleto(Habilidade):
    def __init__(self):
        super().__init__("Invocação de Esqueleto", 15, "Dano moderado e ganha Escudo Endurecido (Defesa Temporária).")
    def usar(self, atacante, alvo):
        if super().usar(atacante, alvo):
            dano = atacante.ataque * 1.1
            alvo.vida -= dano
            bonus_defesa = dano * 0.5
            atacante.defesa_extra_turno = bonus_defesa
            print(f"☠️ {atacante.nome} invoca um Esqueleto, causando {dano:.0f} de dano e ganhando +{bonus_defesa:.0f} de Defesa temporária.")
            return True
        return False

class ChamaProfana(Habilidade):
    def __init__(self):
        super().__init__("Chama Profana", 10, "Atinge o alvo com dano por tempo (DoT).")
    def usar(self, atacante, alvo):
        if super().usar(atacante, alvo):
            alvo.dot_profano = 7 
            print("🔥 O alvo está ardendo em Chamas Profanas!")
            return True
        return False

# ARCANIST (Crux System)
class FluxoArcano(Habilidade):
    def __init__(self):
        super().__init__("Fluxo Arcano", 5, "Gera 1 Ponto Crux (máx 3) e causa dano leve.")
    def usar(self, atacante, alvo):
        if super().usar(atacante, alvo):
            atacante.crux = min(3, getattr(atacante, 'crux', 0) + 1) 
            dano = 5
            alvo.vida -= dano
            print(f"🌀 {atacante.nome} usa Fluxo Arcano, gerando 1 Crux ({atacante.crux}/3) e causando {dano:.0f} de dano.")
            return True
        return False

class RaioDoDestino(Habilidade):
    def __init__(self):
        super().__init__("Raio do Destino", 20, "Causa dano massivo. Consome todos os Pontos Crux para dano bônus.")
    def usar(self, atacante, alvo):
        if super().usar(atacante, alvo):
            crux_consumido = getattr(atacante, 'crux', 0)
            dano_base = atacante.ataque * 0.7
            dano_bonus = crux_consumido * 15 
            dano_total = dano_base + dano_bonus
            
            print(f"💥 Consome {crux_consumido} Crux para poder total!")
            atacante.crux = 0
            
            alvo.vida -= dano_total
            print(f"🔮 {atacante.nome} invoca o Raio do Destino, causando {dano_total:.0f} de dano MÁGICO!")
            return True
        return False