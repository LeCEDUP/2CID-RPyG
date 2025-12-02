# Desenvolva o seu jogo aqui
def menu_principal():
    print("MENU PRINCIPAL ")
    print("1  Explorar")
    print("2  Ver status")
    print("3  Inventário")
    print("4  Sair")
    return input("Escolhe uma opção: ")

from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro

alice = Heroi("Alice", 100, 12, 5)
valete = Monstro("Valete de Copas", 40, 8, 3, "Pequeno")
rainha = Monstro("Rainha Vermelha", 50, 12, 6, "Pequeno")
jaguadarte = Monstro("Jaguadarte", 150, 20, 10, "Lendário")

espada = Arma("Espada de Vorpal", "A única espada capaz de matar o Jaguadarte.", 10)
armadura = Armadura("Armadura Prata", "Traje feito pela Rainha Branca para Alice.", 5)
pocao_vida = Item("Poção de Cura", "Restaura 30 de vida.")

print("Início da Jornada")
print("Você é Alice, e retornou ao País das Maravilhas para acabar com a tirania da Rainha Vermelha!")
input("Aperte ENTER para se aventurar.")

alice.inventario.append(espada)
alice.inventario.append(armadura)
alice.inventario.append(pocao_vida)
alice.equipar_item(espada)
alice.equipar_item(armadura)

while True:
    escolha = menu_principal()

    if escolha == "1":
        print("Você decide explorar o País das Maravilhas.")
        
        print("Batalha contra o Valete de Copas ")
        while alice.esta_vivo() and valete.esta_vivo():
            acao = input("(1) Atacar ou (2) Usar poção? ")
            if acao == "2" and pocao_vida in alice.inventario:
                alice.vida += 30
                alice.inventario.remove(pocao_vida)
                print(f"{alice.nome} usou uma poção e recuperou vida! ({alice.vida} de vida)")
            else:
                alice.atacar(valete)
            if valete.esta_vivo():
                valete.atacar(alice)

        if not alice.esta_vivo():
            print(f"{alice.nome} foi derrotada pelo {valete.nome}. Fim da aventura.")
            break
        else:
            print(f"{alice.nome} derrotou o {valete.nome}! Ganhou 50 de experiência.")
            alice.ganhar_experiencia(50)
        
     
        print(" Batalha contra a Rainha Vermelha ")
        while alice.esta_vivo() and rainha.esta_vivo():
            acao = input("(1) Atacar ou (2) Defender? ")
            if acao == "2":
                print(f"{alice.nome} se defende e reduz o dano!")
                alice.defesa += 3
            else:
                alice.atacar(rainha)
            if rainha.esta_vivo():
                rainha.atacar(alice)
                alice.defesa = 5

        if not alice.esta_vivo():
            print(f"{alice.nome} foi derrotada pela {rainha.nome}. Fim da aventura.")
            break
        else:
            print(f"A {rainha.nome} foi derrotada! O verdadeiro inimigo ainda a espera.")
            alice.ganhar_experiencia(100)

       
        print("Batalha Final: O Jaguadarte acorda ")
        while alice.esta_vivo() and jaguadarte.esta_vivo():
            acao = input("(1) Atacar ou (2) Usar poção (se tiver)? ")
            if acao == "2" and any(i.nome == "Poção de Cura" for i in alice.inventario):
                alice.vida += 30
                for i in alice.inventario:
                    if i.nome == "Poção de Cura":
                        alice.inventario.remove(i)
                        break
                print(f"{alice.nome} usou uma poção! Vida atual: {alice.vida}")
            else:
                alice.atacar(jaguadarte)
            if jaguadarte.esta_vivo():
                jaguadarte.atacar(alice)

        if alice.esta_vivo():
            print(f"Parabéns, {alice.nome}! Você derrotou o {jaguadarte.nome} e libertou o País das Maravilhas!")
            alice.ganhar_experiencia(300)
        else:
            print(f"{alice.nome} foi derrotada pelo {jaguadarte.nome}. Fim da jornada.")
        print(" Fim da Aventura ")
        break

    elif escolha == "2":
        print(f"Status de {alice.nome}: Vida = {alice.vida}, Ataque = {alice.ataque}, Defesa = {alice.defesa}")

    elif escolha == "3":
        print("Inventário:")
        for item in alice.inventario:
            print(f"- {item.nome}: {item.descricao}")

    elif escolha == "4":
        print("Saindo da aventura, até logo, viajante!")
        break

    else:
        print("Opção inválida. Tente novamente.")
