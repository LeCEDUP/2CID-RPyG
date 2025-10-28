

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



