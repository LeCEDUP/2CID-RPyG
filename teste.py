from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro
import random
import time


def pausa(texto="..."):
    time.sleep(1)
    print(texto)
    time.sleep(1)


def menu():
    print("\n=== THE LEGEND OF THE COSMIC HUNTER ===")
    print("1 - Criar Caçador")
    print("2 - Iniciar Missão")
    print("3 - Acessar Loja")
    print("4 - Status do Caçador")
    print("5 - Sair")


def criar_heroi():
    nome = input("Digite o nome do seu caçador: ").capitalize()
    heroi = Heroi(nome, 120, 20, 8)
    heroi.drhokens = 100  # moedas iniciais
    print(f"\nBem-vindo, {heroi.nome}! Um novo caçador de recompensas no universo cósmico.")
    return heroi


def gerar_inimigo(nivel_heroi):
    tipos = [
        ("Alien Rastejante", 60 + nivel_heroi * 5, 10 + nivel_heroi * 2, 5 + nivel_heroi),
        ("Droide de Combate", 90 + nivel_heroi * 8, 15 + nivel_heroi * 2, 8 + nivel_heroi),
        ("Caçador Pirata", 120 + nivel_heroi * 10, 20 + nivel_heroi * 3, 10 + nivel_heroi),
    ]
    nome, vida, ataque, defesa = random.choice(tipos)
    return Monstro(nome, vida, ataque, defesa, "Médio")


def batalha(heroi, monstro):
    print(f"\n🚨 Encontro! {heroi.nome} enfrenta {monstro.nome}!")
    while heroi.esta_vivo() and monstro.esta_vivo():
        heroi.atacar(monstro)
        pausa()
        if monstro.esta_vivo():
            monstro.atacar(heroi)
            pausa()

    if heroi.esta_vivo():
        recompensa_xp = random.randint(40, 90)
        recompensa_drhokens = random.randint(30, 80)
        heroi.ganhar_experiencia(recompensa_xp)
        heroi.drhokens += recompensa_drhokens
        print(f"\n✅ Missão completa! Você ganhou {recompensa_xp} XP e {recompensa_drhokens} Drhokens.")
        return True
    else:
        print(f"\n💀 {heroi.nome} foi derrotado pelo {monstro.nome}...")
        return False


def loja(heroi):
    loja_itens = [
        Arma("Pistola de Laser", "Arma padrão de energia.", 8, preco=50),
        Arma("Rifle de Plasma", "Dispara rajadas concentradas.", 15, preco=120),
        Armadura("Armadura de Doom", "Proteção lendária da era antiga.", 12, preco=150),
        Item("RedBull", "Restaura 40 de vida instantaneamente.", preco=30)
    ]

    print("\n=== Loja Cósmica ===")
    print(f"Drhokens disponíveis: {heroi.drhokens}")
    for i, item in enumerate(loja_itens, start=1):
        print(f"{i} - {item.nome} ({item.__class__.__name__}) - {item.preco} Drhokens")

    escolha = input("Digite o número do item para comprar ou 0 para sair: ")
    if escolha == "0":
        return

    try:
        item_escolhido = loja_itens[int(escolha) - 1]
        if heroi.drhokens >= item_escolhido.preco:
            heroi.drhokens -= item_escolhido.preco
            heroi.inventario.append(item_escolhido)
            print(f"🛒 Você comprou {item_escolhido.nome}!")
        else:
            print("❌ Drhokens insuficientes!")
    except (IndexError, ValueError):
        print("Opção inválida.")


def usar_item(heroi):
    redbulls = [i for i in heroi.inventario if i.nome == "RedBull"]
    if not redbulls:
        print("Você não tem RedBull no inventário!")
        return
    heroi.vida += 40
    if heroi.vida > heroi.vida_maxima:
        heroi.vida = heroi.vida_maxima
    heroi.inventario.remove(redbulls[0])
    print(f"⚡ {heroi.nome} bebeu um RedBull! Vida atual: {heroi.vida}")


def mostrar_status(heroi):
    print("\n=== STATUS DO CAÇADOR ===")
    print(f"Nome: {heroi.nome}")
    print(f"Nível: {heroi.nivel}")
    print(f"Vida: {heroi.vida}/{heroi.vida_maxima}")
    print(f"Ataque: {heroi.ataque}")
    print(f"Defesa: {heroi.defesa}")
    print(f"Experiência: {heroi.experiencia}/100")
    print(f"Drhokens: {heroi.drhokens}")
    print(f"Itens: {[i.nome for i in heroi.inventario]}")


def aventura(heroi):
    print("\n--- Iniciando missão de caça ---")
    inimigo = gerar_inimigo(heroi.nivel)
    if batalha(heroi, inimigo):
        # Chance de ganhar um item
        if random.random() < 0.3:
            novo_item = Item("RedBull", "Restaura 40 de vida.")
            heroi.inventario.append(novo_item)
            print("🍾 Você encontrou um RedBull após a missão!")


def main():
    heroi = None
    while True:
        menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            heroi = criar_heroi()
        elif opcao == "2":
            if heroi:
                aventura(heroi)
            else:
                print("Crie um caçador primeiro!")
        elif opcao == "3":
            if heroi:
                loja(heroi)
            else:
                print("Crie um caçador primeiro!")
        elif opcao == "4":
            if heroi:
                mostrar_status(heroi)
                usar = input("Deseja usar um RedBull? (s/n): ").lower()
                if usar == "s":
                    usar_item(heroi)
            else:
                print("Crie um caçador primeiro!")
        elif opcao == "5":
            print("Encerrando o jogo... Que a Força Cósmica esteja com você.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
