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
