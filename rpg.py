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

        while hollow["hp"] > 0 and player_hp > 0:
            print("\n" + "-" * 60)
            print(f"Sua Vida: {player_hp} | Vida do {hollow['nome']}: {hollow['hp']}")
            print("1️⃣ Atacar")
            print("2️⃣ Defender")
            print("3️⃣ Concentrar reishi (Curar)")
            print("4️⃣ Fugir")
            escolha = input("\nO que deseja fazer? ")

            if escolha == "1":
                dano_causado = random.randint(player_dano - 5, player_dano + 5)
                hollow["hp"] -= dano_causado
                narrar(f"\nVocê ataca com sua zanpakutō e causa {dano_causado} de dano!")

                elif escolha == "2":
                narrar("\nVocê assume uma postura defensiva, preparando-se para o ataque.")
                defesa = True

                elif escolha == "3":
                player_hp += cura
                if player_hp > 100:
                    player_hp = 100
                narrar(f"\nVocê canaliza seu reishi e recupera {cura} pontos de vida!")

                elif escolha == "4":
                narrar("\nVocê tenta recuar, mas o Hollow bloqueia seu caminho!")
                continue

                else:
                narrar("\nOpção inválida!")
                continue
