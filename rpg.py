# Desenvolva o seu jogo aqui
from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro

# ===========================
# 🔥 RPG DRAGON BALL 
# ===========================

print("🌌 --- BATALHA PELO UNIVERSO: DRAGON BALL SUPER --- 🌌")
print("Prepare-se para lutar pela sobrevivência de todos os universos!")

# Criando personagens
heroi = Heroi("Goku (Ultra Instinct)", 500, 70, 25)
jiren = Monstro("Jiren", 450, 85, 30, "Gigante")
black_freeza = Monstro("Black Freeza", 600, 90, 35, "Grande")
vegeta = Heroi("Vegeta (Ultra Ego)", 480, 75, 22)
# Criando itens
kamehameha = Arma("Kamehameha", "Golpe icônico de Goku, carregado com energia divina.", 40)
armadura_treinamento = Armadura("Gi de Treinamento do Whis", "Uniforme divino que aumenta a defesa.", 20)
senzu = Item("Semente dos Deuses", "Restaura completamente a vida.")

# ===========================
# 🌠 Introdução
# ===========================

print(f"\n{heroi.nome} desperta em meio a um novo torneio dos deuses...")
input("Pressione ENTER para continuar...")

print(f"\nWhis entrega a {heroi.nome} um {kamehameha.nome}, um {armadura_treinamento.nome} e uma {senzu.nome}!")
heroi.inventario += [kamehameha, armadura_treinamento, senzu]

# Equipar
heroi.equipar_item(kamehameha)
heroi.equipar_item(armadura_treinamento)

print("\nGoku entra em posição de combate. A arena treme... surge Jiren!")
input("Pressione ENTER para iniciar a luta contra Jiren!")
# ===========================
# 🥊 Batalha 1: Goku vs Jiren
# ===========================
while heroi.esta_vivo() and jiren.esta_vivo():
    print(f"\nVida de {heroi.nome}: {heroi.vida} | Vida de {jiren.nome}: {jiren.vida}")
    acao = input("\nEscolha sua ação: [1] Atacar [2] Defender [3] Usar Semente: ")

    if acao == "1":
        heroi.atacar(jiren)
    elif acao == "2":
        print(f"{heroi.nome} assume postura defensiva! Reduz o dano neste turno.")
        if jiren.esta_vivo():
            dano = jiren.ataque - (heroi.defesa * 2)
            if dano < 0: dano = 0
            heroi.vida -= dano
            print(f"{jiren.nome} ataca causando {dano} de dano reduzido!")
        continue
    elif acao == "3" and senzu in heroi.inventario:
        heroi.vida = 500
        heroi.inventario.remove(senzu)
        print(f"{heroi.nome} come uma {senzu.nome} e restaura totalmente a vida!")
    else:
        print("Ação inválida!")

    if jiren.esta_vivo():
        jiren.atacar(heroi)
# Pós-luta
if heroi.esta_vivo():
    print(f"\n🔥 {heroi.nome} derrotou Jiren! O campo inteiro vibra de energia!")
    heroi.ganhar_experiencia(300)
else:
    print(f"\n💀 {heroi.nome} caiu diante do poder de {jiren.nome}... Fim de jogo.")
    exit()

# ===========================
# 🌱 Recuperação
# ===========================
print("\nApós a luta, {heroi.nome} sente o Ki de alguém poderoso se aproximando...")
input("Pressione ENTER para continuar...")

print("\n⚠️ Black Freeza aparece! A ameaça suprema retorna para destruir tudo!")
print("Mas Vegeta chega para ajudar! 👑🔥")
# ===========================
# 💥 Batalha Final
# ===========================
turno = 1
while (heroi.esta_vivo() or vegeta.esta_vivo()) and black_freeza.esta_vivo():
    print(f"\n--- TURNO {turno} ---")
    print(f"Vida: {heroi.nome}({heroi.vida}) | Vegeta({vegeta.vida}) | Black Freeza({black_freeza.vida})")

    acao = input(f"\nEscolha sua ação para {heroi.nome}: [1] Atacar [2] Defender: ")
    if acao == "1":
        heroi.atacar(black_freeza)
    elif acao == "2":
        print(f"{heroi.nome} concentra energia e reduz o dano recebido neste turno.")
    else:
        print("Ação inválida, você hesitou no combate!")

    if vegeta.esta_vivo() and black_freeza.esta_vivo():
        print(f"\n{vegeta.nome} avança com um golpe feroz!")
        vegeta.atacar(black_freeza)

    if black_freeza.esta_vivo():
        alvo = vegeta if turno % 2 == 0 and vegeta.esta_vivo() else heroi
        black_freeza.atacar(alvo)

    turno += 1
