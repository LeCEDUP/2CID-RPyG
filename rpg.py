from personagens.heroi import Heroi
from personagens.monstro import Monstro
from itens.arma import Arma
from itens.armadura import Armadura
from itens.item import Item
import random

# Configuração do jogo
heroi = Heroi(input("Nome do Caçador: "), 100, 15, 5)
drhokens = 100
planeta_atual = "Tatooine"
nivel_missao = 0

# Planetas disponíveis (mantido para referência de dificuldade)
planetas = {
    "Tatooine": {"dificuldade": 1, "recompensa": 1.0},
    "Coruscant": {"dificuldade": 2, "recompensa": 1.5},
    "Kashyyyk": {"dificuldade": 3, "recompensa": 2.0},
    "Mustafar": {"dificuldade": 4, "recompensa": 3.0}
}

# Inimigos por dificuldade
inimigos = [
    [Monstro("Alien Zergon", 50, 10, 3, "Alien"), Monstro("Mercenário", 60, 12, 4, "Humano")],
    [Monstro("Robô Assassino", 80, 15, 5, "Robô"), Monstro("Caçador Droide", 90, 16, 6, "Droide")],
    [Monstro("Wookie Fugitivo", 110, 18, 7, "Wookie"), Monstro("Jedi Caído", 120, 20, 8, "Jedi")],
    [Monstro("Lorde Sith", 150, 25, 10, "Sith"), Monstro("General Imperial", 140, 22, 9, "Imperial")]
]

# Bosses dos planetas
bosses = [
    Monstro("CHEFE: Gangster Hutt", 200, 30, 12, "Hutt"),
    Monstro("CHEFE: Mestre do Crime", 250, 35, 15, "Crime"),
    Monstro("CHEFE: Rei Wookie", 300, 40, 18, "Wookie"),
    Monstro("CHEFE: Imperador Sith", 400, 50, 25, "Sith")
]

# Loja com mais itens
loja = [
    Arma("Blaster", "Arma laser básica", 12),
    Arma("Rifle Laser", "Rifle de precisão", 18),
    Arma("Sabre Luz", "Espada de energia Jedi", 25),
    Arma("Lançador", "Arma pesada destrutiva", 35),
    Armadura("Traje", "Proteção leve", 8),
    Armadura("Armadura", "Armadura média", 15),
    Armadura("Mandaloriana", "Armadura pesada", 25),
    Item("RedBull", "Energético +40HP"),
    Item("Super RedBull", "Super energético +80HP"),
    Item("Kit Médico", "Cura completa")
]

precos = [60, 120, 200, 300, 50, 100, 180, 30, 60, 150]

# Itens iniciais
heroi.inventario.extend([Item("RedBull", "Energético"), Arma("Blaster", "Arma inicial", 8)])

# História de Início
print("\n" + "="*50)
print("🌟 INÍCIO DA AVENTURA 🌟")
print("="*50)
print(f"\nEm um bar intergaláctico poeirento na periferia de {planeta_atual}, ")
print(f"você, {heroi.nome}, estava recostado no balcão observando a espuma")
print("se dissipar lentamente em seu copo de Grog Astral.")
print("\nO ambiente estava cheio de seres de todos os quadrantes da galáxia -")
print("desde mercenários Twi'lek até contrabandistas Bothan. O cheiro de")
print("combustível de nave e alienígenas sóbrios enchia o ar.")
print("\nFoi então que seus olhos pousaram em um quadro de procurados")
print("iluminado por holoprojeções fracas. Uma recompensa chamou sua atenção:")
print("\n⭐ 'PROCURA-SE: OS MAIS PERIGOSOS DA GALÁXIA' ⭐")
print("\nO valor? Drhokens suficientes para comprar uma lua ou duas.")
print("Sem pensar duas vezes, você decidiu que era sua chance de")
print("se tornar uma lenda...")
print("\nA aventura está prestes a começar!")
input("\nPressione Enter para continuar...")

print(f"\n⭐ CAÇADOR {heroi.nome} INICIADO!")
print(f"📍 Planeta: {planeta_atual}")
print("💰 100 Drhokens • ❤️ 100 Vida")

def batalha_chefe():
    global drhokens
    dificuldade = planetas[planeta_atual]["dificuldade"] - 1
    chefe = bosses[dificuldade]
   
    print(f"\n💀 CHEFE: {chefe.nome} apareceu!")
   
    while heroi.esta_vivo() and chefe.esta_vivo():
        print(f"\n{heroi.nome}: {heroi.vida}HP")
        print(f"{chefe.nome}: {chefe.vida}HP")
       
        acao = input("1-Atacar 2-Item 3-Fugir: ")
       
        if acao == "1":
            heroi.atacar(chefe)
            if chefe.esta_vivo():
                chefe.atacar(heroi)
        elif acao == "2":
            usar_item()
            if chefe.esta_vivo():
                chefe.atacar(heroi)
        elif acao == "3":
            print("🏃 Fugiu do chefe!")
            return False
   
    if heroi.esta_vivo():
        recompensa = 500 * (dificuldade + 1)
        drhokens += recompensa
        heroi.ganhar_experiencia(200 * (dificuldade + 1))
        print(f"🎉 CHEFE DERROTADO! +{recompensa}💰")
        return True
    return False

def usar_item():
    itens_uso = [item for item in heroi.inventario if "RedBull" in item.nome or "Kit" in item.nome]
   
    if not itens_uso:
        print("❌ Sem itens de cura!")
        return
   
    print("\n🎒 Itens disponíveis:")
    for i, item in enumerate(itens_uso):
        print(f"{i+1}. {item.nome}")
   
    try:
        escolha = int(input("Usar item: ")) - 1
        if 0 <= escolha < len(itens_uso):
            item = itens_uso[escolha]
            if "Super" in item.nome:
                heroi.vida += 80
            elif "Kit" in item.nome:
                heroi.vida = 100 + (heroi.nivel * 20)
            else:
                heroi.vida += 40
            heroi.inventario.remove(item)
            print(f"✅ Usou {item.nome}!")
    except:
        print("❌ Inválido!")