import random
import time

def narrar(texto, atraso=0.04):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(atraso)
    print()

def introducao():
    print("=" * 60)
    print("               🌑 ECOS DO OUTRO LADO 🌑")
    print("=" * 60)
    time.sleep(1.5)

    narrar("\nO mundo é muito maior do que você imagina...")
    narrar("Além do que os olhos podem ver, há algo oculto.")
    narrar("Um véu separa a realidade do desconhecido.")
    narrar("Alguns chamam de inferno. Outros, de O Outro Lado.")
    narrar("Mas a verdade é uma só: o Paranormal é real.")
    time.sleep(2)

    print("\n" + "-" * 60 + "\n")
    narrar("Você é um agente da ORDO REALITAS — uma organização que investiga e combate o paranormal.")
    narrar("Há dias, uma série de desaparecimentos vem ocorrendo na pequena cidade de Vila do Sol.")
    narrar("Pessoas foram vistas vagando à noite... com olhos vazios e marcas negras na pele.")
    narrar("A última gravação de rádio antes do silêncio dizia apenas: 'Ele está voltando.'")
    time.sleep(2)

    narrar("\nSua missão é simples: investigar, sobreviver e impedir que o Outro Lado se abra.")
    narrar("Mas cuidado... o Véu está enfraquecido.")
    time.sleep(2)
    print("\n" + "=" * 60)
    narrar("Pressione ENTER para continuar...")
    input()