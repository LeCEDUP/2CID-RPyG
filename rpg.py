#Função para narrar

import random
import time

def narrar(texto, atraso=0.04):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(atraso)
    print()

def introducao():
    print("=" * 60)
    print("               🌑 ECOS DO OUTRO LADO 🌑")
    print("=" * 60)
    time.sleep(1.5)

    narrar("\nO mundo é muito maior do que você imagina...")
    narrar("Além do que os olhos podem ver, há algo oculto.")
    narrar("Um véu separa a realidade do desconhecido.")
    narrar("Alguns chamam de inferno. Outros, de O Outro Lado.")
    narrar("Mas a verdade é uma só: o Paranormal é real.")
    time.sleep(2)

    print("\n" + "-" * 60 + "\n")
    narrar("Você é um agente da ORDO REALITAS — uma organização que investiga e combate o paranormal.")
    narrar("Há dias, uma série de desaparecimentos vem ocorrendo na pequena cidade de Vila do Sol.")
    narrar("Pessoas foram vistas vagando à noite... com olhos vazios e marcas negras na pele.")
    narrar("A última gravação de rádio antes do silêncio dizia apenas: 'Ele está voltando.'")
    time.sleep(2)

    narrar("\nSua missão é simples: investigar, sobreviver e impedir que o Outro Lado se abra.")
    narrar("Mas cuidado... o Véu está enfraquecido.")
    time.sleep(2)
    print("\n" + "=" * 60)
    narrar("Pressione ENTER para continuar...")
    input()

#Jogo principal

def jogo():
    print("\n=== MISSÃO: VILA DO SOL ===")
    nome = input("Digite o nome do seu agente: ")
    print(f"Bem-vindo, Agente {nome}.\n")

    print("Escolha sua Classe:")
    print("1 - Combatente 🪖 (força física, alta resistência)")
    print("2 - Ocultista 📖 (usa o paranormal, mas arrisca a sanidade)")
    print("3 - Especialista 🧰 (mais evasivo e estratégico)")

    classe = input("Escolha (1/2/3): ")

    #Atributos de classe

#combatente
    if classe == "1":
        vida_jogador = 45
        sanidade = 80
        evasao = 0.10
        defesa = 0.25
        arma = "Pistola e Faca Militar"
#ocultista
    elif classe == "2":
        vida_jogador = 30
        sanidade = 100
        evasao = 0.15
        defesa = 0.10
        arma = "Ritual e Símbolos Arcanos"
#Especialista
    else:
        vida_jogador = 35
        sanidade = 90
        evasao = 0.25
        defesa = 0.15
        arma = "Gadgets e Ferramentas"

    vida_inimigo = 45
    nome_inimigo = "Aberração do Véu"
    inventario = {"poções": 2, "talismãs": 1, "ouro": 0}

    narrar(f"\nVocê entra nas ruínas da antiga capela de Vila do Sol, empunhando {arma.lower()}...")
    narrar("O ar é denso... algo sussurra seu nome. Um portal instável brilha na parede rachada.")
    time.sleep(2)
    narrar(f"De dentro dele, surge uma forma distorcida: {nome_inimigo}.")
    time.sleep(1)

#Função de combate

    while vida_jogador > 0 and vida_inimigo > 0:
            print(f"\n{name_format(nome)}: {vida_jogador} ❤️ | Sanidade: {sanidade}% 🧠")
            print(f"{nome_inimigo}: {vida_inimigo} 💀")
            print(f"Inventário: {inventario}")
            acao = input("\nAtacar (a), Curar (c), Defender (d), Usar Talismã (t) ou Fugir (f)? ").lower()

    if acao == "a":
                if classe == "1":  # Combatente
                    if random.random() < 0.15:
                        dano = 0
                        print("Você errou o disparo!")
                    else:
                        dano = random.randint(5, 9)
                        if random.random() < 0.20:
                            dano += random.randint(3, 5)
                            print("Ataque preciso! Você atingiu um ponto vital!")
                    print(f"Você causou {dano} de dano!")
                elif classe == "2":  # Ocultista
                    if random.random() < 0.25:
                        dano = random.randint(8, 12)
                        print("Você canaliza energia paranormal! 🔮")
                        sanidade -= random.randint(5, 10)
                    else:
                        dano = random.randint(4, 7)
                        print("Você lança um feitiço menor.")
                    print(f"Você causou {dano} de dano!")
                else:  # Especialista
                    if random.random() < 0.10:
                        dano = 0
                        print("Seu ataque falhou!")
                    else:
                        dano = random.randint(3, 6)
                        if random.random() < 0.35:
                            dano *= 2
                            print("Ataque crítico com precisão cirúrgica! ⚡")
                    print(f"Você causou {dano} de dano!")

                vida_inimigo -= dano

#Evento paranormal
                if random.random() < 0.20:
                    print("\n⚠️ A criatura distorce o ambiente!")
                    dano_mental = random.randint(5, 15)
                    sanidade -= dano_mental
                    print(f"Sua mente treme... perdeu {dano_mental}% de sanidade!")

            # Cura

                elif acao == "c":
                    if inventario["poções"] > 0:
                        cura = random.randint(5, 10)
                        vida_jogador += cura
                        inventario["poções"] -= 1
                        print(f"Você usou um kit médico e recuperou {cura} de vida!")
                    else:
                        print("Você não tem mais poções!")

            # Defesa
                elif acao == "d":
                    print("Você assume uma posição defensiva, focando em resistir. 🛡️")
                    defesa_turno = True

            # Talismã
                elif acao == "t":
                    if inventario["talismãs"] > 0:
                        print("Você ergue um talismã contra o Véu! ✴️")
                        inventario["talismãs"] -= 1
                        dano = random.randint(6, 12)
                        vida_inimigo -= dano
                        sanidade += random.randint(5, 10)
                        print(f"A energia espiritual queimou a criatura e restaurou parte da sua mente! (+Sanidade)")
                    else:
                        print("Você não tem mais talismãs!")

            # Fuga
                elif acao == "f":
                    narrar("Você recua, sentindo o peso das vozes do Outro Lado...")
                    break
                else:
                    print("Ação inválida!")
                    continue

            # Ataque do inimigo
                if vida_inimigo > 0:
                    print(f"\n{name_format(nome_inimigo)} ruge e avança!")
                    if random.random() < evasao:
                        print("Você esquivou por pouco! 💨")
                    else:
                        dano_inimigo = random.randint(4, 9)
                        if acao == "d":
                            dano_inimigo = int(dano_inimigo * (1 - defesa))
                            print("Sua defesa reduziu parte do dano!")
                        vida_jogador -= dano_inimigo
                        print(f"A aberração causou {dano_inimigo} de dano!")
                        if random.random() < 0.2:
                            print("Seu corpo arrepia... algo sussurra em sua mente.")
                            sanidade -= random.randint(5, 10)

            # Verificar sanidade
                if sanidade <= 0:
                    narrar("\nVocê perdeu completamente a sanidade...")
                    narrar("O Véu se abre diante de você. E desta vez... você atravessa.")
                    vida_jogador = 0
                    break