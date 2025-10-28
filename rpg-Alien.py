from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro
import time
import random

def menu_principal():
    print("\n=== ALIEN: O 8.º PASSAGEIRO ===")
    print("1 - Iniciar Missão")
    print("2 - Sair")
    escolha = input("Escolha uma opção: ")
    
def criar_tripulante():
        nome = input("\nDigite o nome do tripulante: ")
        tripulante = Heroi(nome, 100, 15,3)
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
        Arma("Lança-chamas", "Uma arma improvisada, eficaz contra o alien.", 12),
        Item("Kit Médico", "Restaura 40 de vida."),
        Armadura("Traje Espacial", "Protege contra ataques ácidos.", 6)
    ]
    item = random.choice(possiveis_itens)
    print(f"\nNo {rota_descricao(rota)}, {tripulante.nome} encontrou um {item.nome}!")
    escolha = input("Deseja pegar o item? (s/n): ").lower()
    if escolha == "s":
        tripulante.inventario.append(item)
        print(f"{item.nome} adicionado ao inventário.")
    else:
        print("Você deixou o item para trás...")
    return True

def evento_combate(tripulante, rota):
    inimigos = [
        Monstro("facehugger", 25, 8, 1, "pequeno"),
        Monstro("Xenomorfo", 80, 20, 5, "Médio"),
        Monstro("Rainha Alien", 180, 30, 8, "Gigante")
    ]
    inimigo = random.choice(inimigos)
    print(f"\n⚠ ALERTA: {tripulante.nome} encontrou um {inimigo.nome} no {rota_descricao(rota)}!")
    return batalha(tripulante, inimigo) 

def batalha(heroi, monstro):
    print(f"\n--- Combate: {heroi.nome} vs {monstro.nome} ---")
    while heroi.esta_vivo() and monstro.esta_vivo():
        heroi.atacar(monstro)
        time.sleep(1)
        if monstro.esta_vivo():
            monstro.atacar(heroi)
            time.sleep(1)
    if heroi.esta_vivo():
        print(f"\n{heroi.nome} sobreviveu ao ataque do {monstro.nome}!")
        heroi.ganhar_experiencia(50)
        return True
    else:
        print(f"\nO {monstro.nome} matou {heroi.nome}. A missão terminou...")
        return False
    
def rota_descricao(rota):
    if rota == "1":
        return "Laboratório de espécimes"
    elif rota == "2":
        return "Sala de máquinas"
    elif rota == "3":
        return "Cabine de comando"
    return "Corredor escuro"

def usar_item(tripulante):
    for item in tripulante.inventario:
        if "kit" in item.nome.lower():
            tripulante.vida += 40
            tripulante.inventario.remove(item)
            print(f"{tripulante.nome} usou {item.nome}. Vida atual: {tripulante.vida}")
            return
    print("Você não tem nenhum kit médico.")

def jogo():
    escolha = menu_principal()
    if escolha == "2":
        print("Encerrando o protocolo da Nostromo...")
        return

    tripulante = criar_tripulante()

    print("\nEquipando traje padrão e ferramentas de bordo...")
    tripulante.inventario.extend([
        Arma("Cano de Ferro", "Ferramenta improvisada.", 5),
        Item("Kit Médico", "Restaura 40 de vida.")
    ])

    print("\nO sistema de suporte de vida está falhando... sobreviva e elimine o que está a bordo.")
    while tripulante.esta_vivo():
        print("\n============================")
        print(f"Vida: {tripulante.vida} | Inventário: {[item.nome for item in tripulante.inventario]}")
        print("============================")
        print("1 - Explorar a nave")
        print("2 - Usar Kit Médico")
        print("3 - Encerrar missão")
        acao = input("Escolha uma ação: ")

        if acao == "1":
            if not explorar(tripulante):
                break
        elif acao == "2":
            usar_item(tripulante)
        elif acao == "3":
            print("\nVocê entrou em hibernação. Missão abortada.")
            break
        else:
            print("Comando inválido.")

    print("\n--- Fim da Missão ---")

# -------------------- EXECUÇÃO --------------------
if __name__ == "__main__":
    jogo()