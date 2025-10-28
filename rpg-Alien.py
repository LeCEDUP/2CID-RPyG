from personagens.heroi import Heroi
from itens.arma import Arma
from personagens.monstro import Monstro

def menu():
    print('---Alien, o 8.º Passageiro pt2---')
    print('----------------------')
    print('----------------------')
    print('----------------------')
    print('----------------------')
    print('----------------------')
    print('----------------------')
    nome_do_heroi = input('digite o nome do seu heroi')
meu_heroi = heroi(nome_do_heroi, 100, 20, 10)
rifle_automatico = Arma("Rifle automático F903WE", "um rifle automático.", 10)
Xenomorfo = Monstro("Xenomorfo", 30, 8, 2, "Um alíenigina ")
armadura_M4X = Armadura("Escudo de Ferro", "Um escudo resistente.", 5)
