# Desenvolva o seu jogo aqui
import time
import random

def narrar(texto, atraso=0.04):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(atraso)
    print()

def introducao():
    print("=" * 60)
    print("                 ⚔️ BLEACH: YŌKOSO! WATASHI NO SŌRU SOCIETY ⚔️") 
    print("=" * 60)
    time.sleep(1.5)

    narrar("\nVocê é um shinigami designado para investigar distorções espirituais em Karakura.")
    narrar("Mas algo está errado. As leituras de reishi estão fora de controle.")
    narrar("De repente... duas presenças surgem — poderosas e famintas.")
    narrar("Hollows.")

    time.sleep(2)
    print("\n" + "=" * 60)
    narrar("Prepare-se para lutar, shinigami.")
    input("\nPressione ENTER para continuar...")

    def combate():
    player_hp = 100
    player_dano = 20
    cura = 15

    hollows = [
        {"nome": "Menos Grande", "hp": 60, "dano": 12},
        {"nome": "Adjuchas das Sombras", "hp": 80, "dano": 18}
    ]

    for hollow in hollows:
        narrar(f"\n⚔️ Um {hollow['nome']} surge diante de você!")
        time.sleep(1)