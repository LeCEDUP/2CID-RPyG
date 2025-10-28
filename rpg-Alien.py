from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro
import time

def menu_principal():
    print("\n=== ALIEN: O 8.º PASSAGEIRO ===")
    print("1 - Iniciar Missão")
    print("2 - Sair")
    escolha = input("Escolha uma opção: ")
    
def criar_tripulante():
    def criar_tripulante():
        nome = input("\nDigite o nome do tripulante: ")
        tripulante = heroi(nome, 100, 15,3)
        print(f"\n{tripulante.nome} acorda da criossonia... algo está errado na nave Nostromo.")
        return tripulante   

def iniciar_jogo():
    nome_do_heroi = input('digite o nome do seu heroi')
    meu_heroi = heroi(nome_do_heroi, 100, 20, 10)

def evento_item(tripulante, rota):
    possiveis_itens = [
        Arma("Rifle automático RMC F903WE", "Uma arma improvisada, eficaz contra o alien.", 12),
        Item("Kit Médico", "Restaura 40 de vida."),
        Armadura("Armadura M4X", "Protege contra ataques ácidos e projéteis.", 6)
