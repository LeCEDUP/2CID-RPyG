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

def escolher_rota():
    print("\nVocê está em um corredor escuro da Nostromo. Há três rotas possíveis:")
    print("1 - Laboratório de espécimes")
    print("2 - Sala de máquinas")
    print("3 - Cabine de comando")
    rota = input("Escolha para onde ir (1, 2 ou 3): ")
    return rota

def explorar(tripulante):
    rota = escolher_rota()
    eventos = ["combate", "item", "nada"]
    evento = random.choice(eventos)

    if evento == "combate":
        return evento_combate(tripulante, rota)
    elif evento == "item":
        return evento_item(tripulante, rota)
    else:
        print(f"\n{tripulante,nome} não encontrou nada... apenas o som distante de algo rastejanado")
        return true 

def iniciar_jogo():
    nome_do_heroi = input('digite o nome do seu heroi')
    meu_heroi = heroi(nome_do_heroi, 100, 20, 10)

def evento_item(tripulante, rota):
    possiveis_itens = [
        Arma("Rifle automático RMC F903WE", "Uma arma improvisada, eficaz contra o alien.", 12),
        Item("Kit Médico", "Restaura 40 de vida."),
        Armadura("Armadura M4X", "Protege contra ataques ácidos e projéteis.", 6)
    
