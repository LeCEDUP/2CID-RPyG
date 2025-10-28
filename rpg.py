

from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro

heroi = Heroi("Silas 'Coiote' Graves", 100, 20, 4)
bandido = Monstro("Bandido da Fronteira", 40, 10, 3, "Humano")
chefe_bando = Monstro("Chefe dos Abutres", 150, 25, 8, "Humano")    

revolver = Arma("Revólver Colt", "Um clássico revólver de seis tiros.", 15)
colete = Armadura("Colete de Couro", "Um colete resistente de couro curtido.", 6)
whisky = Item("Garrafa de Whisky", "Recupera 40 pontos de vida.")

print("=== INÍCIO DA AVENTURA NO VELHO OESTE ===\n")

heroi.inventario.append(revolver)
heroi.inventario.append(colete)
heroi.inventario.append(whisky)
print(f"{heroi.nome} encontrou um {revolver.nome}, um {colete.nome} e uma {whisky.nome}.\n")

heroi.equipar_item(revolver)
heroi.equipar_item(colete)

print("--- DUELO NA FRONTEIRA ---")
while heroi.esta_vivo() and bandido.esta_vivo():
    heroi.atacar(bandido)
    if bandido.esta_vivo():
        bandido.atacar(heroi)

if heroi.esta_vivo():
    print(f"{heroi.nome} derrotou o {bandido.nome} no duelo!")
    heroi.ganhar_experiencia(60)
    print(f"Vida atual: {heroi.vida}")
else:
    print(f"{heroi.nome} foi derrubado pelo {bandido.nome}...") 

print("\n--- PAUSA NO SALOON ---")
if whisky heroi.inventario:
    heroi.vida += 40
    heroi.inventario.remove(whisky)
    print(f"{heroi.nome} tomou um {whisky.nome} e recuperou energias. vida atual: {heroi.vida}")
    


