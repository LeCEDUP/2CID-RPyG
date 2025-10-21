# Desenvolva o seu jogo aqui
from personagens.heroi import Heroi
from personagens.monstro import Monstro

def menu():
    print('------------------------')
    print('-----TÍTULO DO JOGO-----')
    print('------------------------')
    print('-------INTRODUÇÃO-------')
    print('-------INTRODUÇÃO-------')
    print('-------INTRODUÇÃO-------')
    print('------------------------')
    nome_do_heroi = input('Digite o nome do seu herói: ')
    meu_heroi = Heroi(nome_do_heroi, 100, 20, 10)
    alien = Monstro("Godofredo", 150, 15, 10, "Alien")

    print("\n--- Batalha contra o Alien ---")
    while meu_heroi.esta_vivo() and alien.esta_vivo():
        escolha = input("Atacar? [s/n]")
        if escolha == 's':
            meu_heroi.atacar(alien)
            if alien.esta_vivo():
                alien.atacar(meu_heroi)
        else:
            print('Fim de Jogo!')

menu()