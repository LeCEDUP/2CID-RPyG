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

