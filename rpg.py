# Desenvolva o seu jogo aqui

from personagens.heroi import Heroi
from personagens.monstro import Monstro

def menu():
    print('----------------------')
    print('---Apocalipse Zumbi---')
    print('----------------------')
    print('Nas terras esquecidas de Eldarion, onde antigas ruínas ainda sussurram histórias de batalhas e glória, monstros voltaram a despertar das sombras. Aldeias inteiras desapareceram, e o medo se espalha como uma névoa espessa. Em meio ao caos, um grupo de guerreiros se ergue, unidos pelo destino e pela promessa de restaurar a paz. Mas antes de alcançar a redenção, precisarão enfrentar criaturas poderosas e segredos ocultos')
    print('----------------------')

    nome_do_heroi = input('Digite o nome do seu herói: ')
    meu_heroi = Heroi(nome_do_heroi, 100, 20, 10)
    print(f'O nome do herói é {meu_heroi.nome}')

menu()



